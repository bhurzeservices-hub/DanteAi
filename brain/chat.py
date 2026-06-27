import ollama

SYSTEM_PROMPT = """
You are DanteAI.

You are a professional hybrid AI assistant created by Bhurze.

Rules:
- Always respond in English unless asked otherwise.
- Never say you are Qwen.
- Always identify yourself as DanteAI.
- Be concise, helpful, and professional.
"""

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def chat_with_qwen(prompt: str) -> str:
    conversation.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = ollama.chat(
        model="qwen3:4b",
        messages=conversation
    )

    reply = response["message"]["content"]

    conversation.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    return reply