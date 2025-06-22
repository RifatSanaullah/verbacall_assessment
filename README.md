Overview
VerbaCall is an intelligent voice assistant system designed to automate and streamline appointment management for medical offices. The system leverages advanced speech-to-text (STT), natural language processing (NLP), and noise-handling strategies to ensure accessibility, accuracy, and reliability—especially for elderly or medically vulnerable patients.

Use Case Scenario
The AI assistant handles inbound patient calls with natural, empathetic conversation, supporting:
- Appointment Booking
- Rescheduling
- Cancellations

The system ensures clarity and avoids hallucinations by confirming ambiguous inputs and avoiding medical advice.

Optimized AI Prompt Design
The assistant’s core behavior is defined by a structured yet simplified prompt optimized from 209 to 142 tokens (32% reduction), preserving essential logic:

Booking: Verifies identity, collects insurance (if new), gathers visit reason, offers 2–3 slots, confirms all details.

Rescheduling: Retrieves and verifies existing appointments, suggests alternatives, confirms changes.
Cancellations: Verifies identity, confirms cancellation intent, offers to reschedule.
Note: The assistant never makes medical decisions—those are referred to doctors.

Adversarial Input Handling
To guard against misunderstood or conflicting speech:

1. Vague Speech Detection
Detected phrases: “thing”, “something”, or hesitation
System prompts:
“Is this about: (1) Booking (2) Symptoms (3) Follow-up?”

2. Conflicting Intent Detection
Detected phrases: “cancel” + “move”
System clarifies:
“Do you want to (1) Cancel or (2) Reschedule?”

This safeguards the system from making invalid or premature actions.

Accent & Noise Handling Pipeline
A robust speech recognition system is deployed using the following architecture:

Components:
Pre-Processing: Noise reduction via noisereduce (Python)


Empirical Evaluation Strategy
The system is tested using realistic multilingual and noisy datasets:

Sample Type	Count
Elderly Bengali-English	10
Elderly Spanish-English	10
Noisy Landline Simulations	5

Key Evaluation Metrics:
Word Error Rate (WER): via jiwer
Intent Accuracy: Correct routing of booking/cancellation/rescheduling flows
Medical Term Precision: Correct interpretation of clinical terminology

Call Session Architecture:
Caller ➝ Voice API ➝ STT Service ➝ GPT Processing ➝ TTS Response ➝ CRM Update

Voice API: Handles call routing and TTS output
STT Service: Combines noise reduction and wav2vec2 for transcription
AI Layer: Interprets user intent and manages conversation
CRM Integration: Logs and updates appointment information

Summary
VerbaCall is a secure, voice-enabled virtual assistant that simplifies patient interaction over the phone. It balances accessibility, clarity, and robustness using real-world STT processing, adversarial intent logic, and multilingual support—all within a privacy-conscious medical context.