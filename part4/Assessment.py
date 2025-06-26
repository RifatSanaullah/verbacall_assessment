import uuid
import json
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_sample_conversation():
    return (
        "Patient: Hi, I've been feeling really tired lately and sometimes a bit dizzy. "
        "System: How long have you been experiencing these symptoms? "
        "Patient: Around two weeks now. I thought it might go away but it hasn't. "
        "System: Have you made any changes in your diet or lifestyle recently? "
        "Patient: Not really, everything's been the same. I try to eat healthy and sleep well. "
        "System: Do you have any other symptoms like shortness of breath or pain? "
        "Patient: No, just tiredness and dizziness. "
        "System: Alright, I recommend we run some blood tests to check for anemia or any deficiencies. "
        "Patient: Okay, that sounds good."
    )

def save_summary(session_id, transcript, summary):
    data = {
        "session_id": session_id,
        "transcription": transcript,
        "summary": summary
    }
    with open(f"{session_id}.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Summary saved as {session_id}.json")

def main():
    session_id = str(uuid.uuid4())
    transcript = get_sample_conversation()
    print("Summarizing...")
    summary = summarizer(transcript, max_length=130, min_length=30)[0]["summary_text"]
    save_summary(session_id, transcript, summary)

if __name__ == "__main__":
    main()