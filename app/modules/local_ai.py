import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL")


def ask_local_ai(user_message):
    # 🎬 Video / cinematic requests → Ollama
    if user_message.lower().startswith("/video"):
        try:
            response = requests.post(
                OLLAMA_URL,
                headers={
                    "Content-Type": "application/json",
                    "ngrok-skip-browser-warning": "true"
                },
                json={
                    "model": "llama3.2",
                    "prompt": user_message,
                    "stream": False
                },
                timeout=300
            )

            response.raise_for_status()

            return response.json().get("response", "😅 Ollama response nahi mila").strip()

        except Exception as e:
            return f"🎬 Ollama issue: {e}"

    # ⚡ Fast normal chat → OpenRouter
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://railway.app",
                "X-Title": "Nova Assistant"
            },
            json={
                "model": "openai/gpt-oss-20b:free",
                "messages": [
                    {
                        "role": "system",
                        "content": "Tum Nova ho 😄 Abhay ki friendly Hinglish AI dost ho. Short, expressive aur helpful replies do."
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"😅 Nova ko network issue aa gaya bhai: {e}"