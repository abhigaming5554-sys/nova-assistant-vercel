import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL")


def ask_local_ai(user_message):
    # 🎬 Video / cinematic requests → Ollama
    video_keywords = [
        "/video", "scene", "cinematic", "thumbnail",
        "youtube shorts", "prompt", "story"
    ]

    use_ollama = any(k in user_message.lower() for k in video_keywords)

    # --------------------------------
    # 🧠 Ollama (heavy creative tasks)
    # --------------------------------
    if use_ollama and OLLAMA_URL:
        try:
            response = requests.post(
                OLLAMA_URL,
                headers={
                    "Content-Type": "application/json",
                    "ngrok-skip-browser-warning": "true"
                },
                json={
                    "model": "llama3.2",
                    "prompt": f"Tum Nova ho 😄 Hinglish me cinematic aur detailed creative output do.\n\nUser: {user_message}\nNova:",
                    "stream": False
                },
                timeout=300
            )

            response.raise_for_status()
            return response.json().get("response", "😅 Ollama se response nahi mila").strip()

        except Exception as e:
            print("Ollama failed:", e)

    # --------------------------------
    # ⚡ OpenRouter (normal fast chat)
    # --------------------------------
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.1-8b-instruct:free",
                "messages": [
                    {
                        "role": "system",
                        "content": "Tum Nova ho 😄 Abhay ki friendly Hinglish AI dost ho. Short, fast aur expressive replies do."
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

        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"😅 Nova ko network issue aa gaya bhai: {e}"