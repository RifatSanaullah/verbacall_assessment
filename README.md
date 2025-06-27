# VerbaCall Assessment

This repository includes a four-part implementation related to AI-driven voice assistants, covering prompt optimization, speech-to-text (STT) processing, call session recovery, and a CLI tool.

---

## Part 1: Prompt Optimization

### Overview
In Part 1, the task was to optimize the prompt without changing its intent or meaning. I used a simple `LLMChain` from LangChain for this purpose.

### Use Case Scenario
The AI assistant handles inbound patient calls with natural, empathetic conversation, supporting:
- Appointment Booking
- Rescheduling
- Cancellations

The system ensures clarity and avoids hallucinations by:
- Confirming ambiguous inputs
- Avoiding any form of medical advice

### Run the Task
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    **N.B.:** Before running, make sure to modify the path inside the `prompt_optimization.py` file as needed.

2. Run the script:
    ```bash
    python prompt_optimization.py
    ```

---

## Part 2: STT Pipeline

### Overview
In Part 2, the task was to implement a Speech-to-Text (STT) pipeline focused on reducing noise and improving recognition accuracy for elderly speech.

### Key Features
- Noise Reduction
- Higher Accuracy for STT
- Better transcription of elderly speech
- Faster processing

### Run the Task
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    **N.B.:** Before running, make sure to modify the path inside the `stt.py` file as needed.

2. Run the script:
    ```bash
    python stt.py
    ```

---

## Part 3: Call Session Recovery

### Overview
In Part 3, the task was to implement a session recovery mechanism by saving user session data including audio and transcribed text.

### Key Features
- Save audio and text under different session IDs
- Retrieve session if user loses connection mid-call

### Run the Task
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    **N.B.:** Before running, make sure to modify the path inside the `session_stt.py` file as needed.

2. Run the script:
    ```bash
    python session_stt.py
    ```

---

## Part 4: Python CLI Tool

### Overview
In Part 4, the task was to develop a Python CLI tool that:
- Takes a `.wav` audio file
- Streams it to an STT engine
- Summarizes the result using GPT
- Saves the output as a JSON log with a session ID

### Run the Task
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    **N.B.:** Before running, make sure to modify the path inside the `Assessment.py` file as needed.

2. Run the script:
    ```bash
    python Assessment.py
    ```