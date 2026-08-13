import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "")


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

            return response.json().get(
                "response",
                "😅 Ollama response nahi mila"
            ).strip()

        except Exception as e:
            return f"🎬 Ollama issue: {e}"

    # ⚡ Fast normal chat → OpenRouter
    try:
        # 🔒 Safety check
        if not OPENROUTER_API_KEY:
            return "❌ OPENROUTER_API_KEY set nahi hai bhai."

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
                        "content": "Tum Nova ho 😄 Friendly Hinglish AI dost ho. Short aur natural replies do."
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            },
            timeout=60
        )

        # ❌ Invalid API key
        if response.status_code == 401:
            return "❌ OpenRouter API key invalid hai bhai. Railway variables check karo."

        # ⏳ Rate limit → Ollama fallback
        if response.status_code == 429:
            try:
                if OLLAMA_URL:
                    ollama_response = requests.post(
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
                        timeout=120
                    )

                    ollama_response.raise_for_status()

                    return ollama_response.json().get(
                        "response",
                        "😅 Ollama fallback bhi reply nahi de paya bhai."
                    ).strip()

            except Exception:
                pass

            return "⏳ Nova thoda busy ho gayi 😅 20-30 second baad try karo bhai."

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"😅 Nova ko network issue aa gaya bhai: {e}"