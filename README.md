**#Verbacall Assessment**


**###Part 1**
**Overview**
    In part 1, the task was to optimize the prompt without changing it's intent or meaning, I tried to optimized the prompt using Simple LLMChain.

    Use Case Scenario
    The AI assistant handles inbound patient calls with natural, empathetic conversation, supporting:
    - Appointment Booking
    - Rescheduling
    - Cancellations

    The system ensures clarity and avoids hallucinations by confirming ambiguous inputs and avoiding medical advice.
    ###Run the task
    - First install `requirements.txt`
    - **N.B.:** Before running, make sure to modify the path inside the `prompt_optimization.py` file as needed.
        
        Run the command:

        ```bash
        python prompt_optimization.py
        ```
**###Part 2**
    In part 2, the task was to implement and design a STT pipeline to reduce the noise and understand the speech of elder people with faster processing.

    Use Case Scenario
    The STT pipeline features are:
    - Noise Reduction
    - Higher Accuracy for STT and noisereduction
    - Easier to convert text for elder people speech
    - Faster Processing for processing the text from speech

    ###Run the task
    - First install `requirements.txt`
    - **N.B.:** Before running, make sure to modify the path inside the `stt.py` file as needed.
        
        Run the command:

        ```bash
        python stt.py
        ```

**###Part 3**
    In part 3, the task was to implement and design a call session recovery task by saving the user session id.

    Use Case Scenario
    The call session recovery pipeline features are:
    - Save Audio, text under different session id
    - if any user lost their connection in the midway, it can be retrived from the database for continuing communication

    ###Run the task
    - First install `requirements.txt`
    - **N.B.:** Before running, make sure to modify the path inside the `session_stt.py` file as needed.
        
        Run the command:

        ```bash
        python session_stt.py
        ```

**###Part 4**
    In part 4, the task was to implement a python CLI tool.

    The tasks are:
    - Takes a .wav file
    - Streams it to STT
    - Summarizes using GPT
    - Saves result as a JSON log with session ID


    ###Run the task
    - First install `requirements.txt`
    - **N.B.:** Before running, make sure to modify the path inside the `Assessment.py` file as needed.
        
        Run the command:

        ```bash
        python Assessment.py
        ```