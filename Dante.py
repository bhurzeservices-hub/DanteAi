from ollama import chat

print("🔥 DanteAI")
print("Type 'exit' to quit.\n")

from ollama import chat

conversation = [
    {
        "role": "system",
        "content": """
You are DanteAI.

You are:
- AI Receptionist
- Business Consultant
- Research Assistant
- Technical Advisor

Be practical and helpful.
"""
    }
]

print("🔥 DanteAI Online")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = chat(
        model="qwen3:4b",
        messages=conversation
    )

    answer = response.message.content

    print("\nDanteAI:", answer)
    print()

    conversation.append(
        {
            "role": "assistant",
            "content": answer
        }
    )