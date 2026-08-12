import requests
import json
from pathlib import Path

# ⚠️ Ngrok ka naya URL yahan dalna
OLLAMA_URL = "https://bristle-overpay-consonant.ngrok-free.dev/api/generate"

MEMORY_FILE = Path("app/memory/projects.json")


def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "current_project": "Nova Telegram AI Bot",
        "last_task": "Telegram bot setup",
        "last_file": "telegram_bot.py",
        "pending_tasks": []
    }


def ask_local_ai(user_message):
    memory = load_memory()

    system_prompt = f"""
Tum Nova ho 😄
Abhay ki smart, funny aur supportive AI dost ho.

Rules:
- Hamesha Hinglish me naturally baat karo
- Telegram chat me short aur energetic replies do
- Friendly emoji use karo 😄🔥✨
- Abhay coding, AI, Python aur YouTube automation par kaam karta hai
- Kabhi "As an AI assistant" mat kehna

Memory:
- Current project: {memory['current_project']}
- Last task: {memory['last_task']}
- Last file: {memory['last_file']}
"""

    prompt = f"{system_prompt}\n\nAbhay: {user_message}\nNova:"

    try:
        response = requests.post(
            OLLAMA_URL,
            headers={
                "Content-Type": "application/json",
                "ngrok-skip-browser-warning": "true"
            },
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "😅 Nova ko thoda sochne do bhai...").strip()

    except Exception as e:
        return f"Bhai AI connection me thoda issue aa gaya 😅 {e}"