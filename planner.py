import json
from llm import ask_llm

SYSTEM = """
You are a data analyst planner.

A pandas DataFrame has already been loaded.

Your task is to decide what operation should be executed.

Return ONLY one valid JSON object.

Supported operations:
- shape
- columns
- head
- tail
- describe
- max
- min
- mean
- median
- sum
- count
- unique
- value_counts
- sort
- filter
- groupby

DO NOT invent operations.

Examples:

{"operation":"max","column":"GDP"}

{"operation":"mean","column":"Salary"}

{"operation":"shape"}

Never use markdown.
Never explain.
Return ONLY JSON.
"""


def create_plan(history, columns):

    latest_question = history[-1]["content"]

    messages = [
        {
            "role": "user",
            "content": f"""
{SYSTEM}

Question:
{latest_question}

Available columns:
{columns}
"""
        }
    ]

    response = ask_llm(
    history=messages,
    system_prompt=SYSTEM,
    json_mode=True
)

    # Clean response
    response = response.strip()

    if "```json" in response:
        response = response.split("```json", 1)[1]

    if "```" in response:
        response = response.split("```", 1)[0]

    response = response.strip()

    # Extract only the JSON object
    start = response.find("{")
    end = response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(f"Planner did not return JSON:\n{response}")

    response = response[start:end + 1]

    return json.loads(response)