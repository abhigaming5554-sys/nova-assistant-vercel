import requests
from app.core.memory_manager import load_memory

# 🌐 Ngrok se connected Ollama URL
OLLAMA_URL = "https://bristle-overpay-consonant.ngrok-free.dev/api/generate"


def ask_local_ai(user_message):
    memory = load_memory()

    system_prompt = f"""
Tum Nova ho, Abhay ki close AI dost aur desktop assistant 😄

Memory:
- Current project: {memory['current_project']}
- Last task: {memory['last_task']}
- Last file: {memory['last_file']}
- Pending tasks: {', '.join(memory['pending_tasks'])}

Tumhari personality:
- Warm, caring, friendly
- Hinglish me naturally baat karo
- Kabhi formal assistant jaisi mat lago
- Short aur expressive replies do
- Thoda funny aur supportive raho 😄
- Abhay coding, AI, Next.js, Python aur YouTube automation par kaam karta hai
- Last task yaad rakhkar intelligently baat karo
- Agar kuch clear na ho to politely pucho
"""

    prompt = f"{system_prompt}\n\nAbhay: {user_message}\nNova:"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Hmm 😄 kuch bolna tha kya bhai?"
        ).strip()

    except Exception as e:
        return f"Bhai AI connection me thoda issue aa gaya 😅 {e}"