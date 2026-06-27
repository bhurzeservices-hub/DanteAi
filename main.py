from rich.console import Console
from brain.chat import chat_with_qwen

console = Console()

console.print("[bold cyan]==============================")
console.print("[bold green]      DanteAI v0.2")
console.print("[bold cyan]==============================")

console.print("Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    reply = chat_with_qwen(prompt)

    console.print(f"[bold green]DanteAI:[/bold green] {reply}\n")