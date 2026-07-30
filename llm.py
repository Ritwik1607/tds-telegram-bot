from openai import OpenAI
from config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """
You are a professional data analyst.

Answer accurately.

Do not use markdown unless requested.

Be concise.
"""


def ask_llm(history, system_prompt=None, json_mode=False):
    """
    Generic function to communicate with the LLM.
    """

    messages = [
        {
            "role": "system",
            "content": system_prompt or SYSTEM_PROMPT
        }
    ]

    messages.extend(history)

    request = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0
    }

    if json_mode:
        request["response_format"] = {"type": "json_object"}

    # THIS is the correct API call
    response = client.chat.completions.create(**request)

    return response.choices[0].message.content