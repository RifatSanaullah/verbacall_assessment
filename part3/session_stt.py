import os
import uuid
import datetime
import torch
import torchaudio
import noisereduce as nr
import redis
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from settings import stt_settings

# Initialize Redis client
redis_client = redis.Redis(
    host=stt_settings["redis_config"]["REDIS_CLIENT"],
    port=stt_settings["redis_config"]["REDIS_PORT"],
    decode_responses=True
)

# Load Wav2Vec2 Model
MODEL_NAME = stt_settings["stt_config"]["model_name"]
device = stt_settings["stt_config"]["device"]
processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_NAME).to(device)
model.eval()

# Preprocessing audio

def preprocess_audio(file_path):
    waveform, sr = torchaudio.load(file_path)
    if sr != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)
        waveform = resampler(waveform)
    audio = waveform[0].numpy()
    reduced_noise = nr.reduce_noise(
        y=audio,
        sr=stt_settings["noise_reduce_config"]["sr"],
        stationary=stt_settings["noise_reduce_config"]["stationary"],
        prop_decrease=stt_settings["noise_reduce_config"]["prop_decrease"],
        n_fft=stt_settings["noise_reduce_config"]["n_fft"],
        win_length=stt_settings["noise_reduce_config"]["win_length"],
        n_std_thresh_stationary=stt_settings["noise_reduce_config"]["n_std_thresh_stationary"]
    )
    return reduced_noise

# Transcription using Wav2Vec2

def transcribe(audio):
    input_values = processor(audio, sampling_rate=16000, return_tensors="pt").input_values.to(device)
    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription.lower()

# Post-process transcription

def post_process(transcription, confidence_score=0.85):
    term_map = {
        "pain pill": "analgesic",
        "bp meds": "hypertension medication",
        "sugar test": "glucose test"
    }
    for k, v in term_map.items():
        transcription = transcription.replace(k, v)
    return transcription

# Main inference and saving pipeline
def run_pipeline(audio_path, session_id=None):
    print(f"\nProcessing: {audio_path}")
    clean_audio = preprocess_audio(audio_path)
    transcription = transcribe(clean_audio)
    final_output = post_process(transcription)

    # Create session id if not given
    if session_id is None:
        session_id = str(uuid.uuid4())

    # Redis Save
    key = f"session:{session_id}"
    existing = redis_client.get(key)
    combined_text = final_output
    if existing:
        combined_text = existing + " " + final_output
    redis_client.set(key, combined_text)

    # File saving
    session_dir = os.path.join("audio_sessions", session_id)
    os.makedirs(session_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename = f"{timestamp}"
    audio_save_path = os.path.join(session_dir, f"{base_filename}.wav")
    text_save_path = os.path.join(session_dir, f"{base_filename}.txt")
    waveform_tensor = torch.from_numpy(np.expand_dims(clean_audio, axis=0))
    torchaudio.save(audio_save_path, waveform_tensor, 16000)
    with open(text_save_path, "w") as f:
        f.write(final_output)

    print(f"Session ID: {session_id}")
    print(f"Saved audio to: {audio_save_path}")
    print(f"Saved transcription to: {text_save_path}")
    print("Combined transcription:", combined_text)

    return session_id, combined_text


if __name__ == "__main__":
    test_files = [
        "/home/mehedi/Rifat/verbacall_assessment/part2/files/harvard.wav",
        "/home/mehedi/Rifat/verbacall_assessment/part2/files/jackhammer.wav",
    ]

    session_id = None
    for file in test_files:
        session_id = str(uuid.uuid4())
        session_id, _ = run_pipeline(file, session_id=session_id)
