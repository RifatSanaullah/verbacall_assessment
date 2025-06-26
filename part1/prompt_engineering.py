def build_optimized_prompt(prompt_text):
    evaluation_query = f"""
Task:
Rewrite the following prompt to reduce its word characters by at least 30% or higher, without losing intent and clarity:

Formatting Rules:
1. Preserve the assistant introduction at the beginning by summarizing it.
2. Maintain section structure with clear headers (like, Greeting:, If booking:, etc.)
3. Keep line breaks (`\\n`) between sections and responses.

What to optimize:
- Reduce repetitive wording and unnecessary modifiers
- Merge similar instructions while preserving empathy and clarity
- Shorten where possible without changing the tone

Clarification Handling (keep these):
If vague speech (like "something", long pause) is detected, respond:
"Just to clarify, what would you like to do today?\n1) Book a new appointment\n2) Reschedule an existing one\n3) Cancel an appointment\nPlease say the number."

If conflicting intent (e.g., both "cancel" and "move" mentioned):
"Let me clarify:\n1) Cancel your appointment\n2) Reschedule to a different time\nPlease say the number you prefer."

Input Prompt:
{prompt_text}

Return only this:
{{
  "optimize_prompt": "<optimized multi-line prompt here, with \\n preserved>" 
}}
"""
    return evaluation_query