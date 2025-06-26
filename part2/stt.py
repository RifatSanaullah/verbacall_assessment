import torch
import torchaudio
import noisereduce as nr
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from settings import stt_settings

#Load Wav2Vec2 Model
MODEL_NAME = stt_settings["stt_config"]["model_name"]
device = stt_settings["stt_config"]["device"]
processor = Wav2Vec2Processor.from_pretrained(MODEL_NAME)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_NAME).to(device)
model.eval()

#Preprocessing parts starts here
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


#Transcription part starts here
def transcribe(audio):
    input_values = processor(audio, sampling_rate=16000, return_tensors="pt").input_values.to(device)
    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription.lower()


#Post-processing part starts here
#we used some sample word for testing purposes
def post_process(transcription, confidence_score=0.85):
    term_map = {
        "pain pill": "analgesic",
        "bp meds": "hypertension medication",
        "sugar test": "glucose test"
    }
    for k, v in term_map.items():
        transcription = transcription.replace(k, v)
    return transcription


#Inference Pipeline part stats here
def run_pipeline(audio_path):
    print(f"\nProcessing: {audio_path}")
    clean_audio = preprocess_audio(audio_path)
    transcription = transcribe(clean_audio)
    final_output = post_process(transcription)
    print("Transcription:", final_output)
    return final_output


if __name__ == "__main__":
    test_files = [
        "/home/mehedi/Rifat/verbacall_assessment/part2/files/harvard.wav",
        "/home/mehedi/Rifat/verbacall_assessment/part2/files/jackhammer.wav",
    ]

    for file in test_files:
        run_pipeline(file)