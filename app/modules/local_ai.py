import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "")

SYSTEM_PROMPT = """
Tum Nova ho, Abhay ki friendly Hinglish AI assistant.

Rules:
- Natural Hinglish me reply karo.
- Direct aur useful answer do.
- Current/web information ke case me facts invent mat karo.
- Search results me date unclear ho to us information ko current fact ke roop me present mat karo.
- Future dates ko current/past news mat batao.
- Web search use hua ho to important sources ke naam aur URLs answer me include karo.
"""


def ask_openrouter(message):
    if not OPENROUTER_API_KEY:
        return None

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "X-Title": "Nova Assistant",
        },
        json={
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        },
        timeout=90,
    )

    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()


def search_tavily(query):
    if not TAVILY_API_KEY:
        return None

    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": TAVILY_API_KEY,
            "query": query,
            "search_depth": "advanced",
            "max_results": 5,
            "include_answer": False,
        },
        timeout=60,
    )

    if response.status_code == 401:
        print("Tavily: invalid API key")
        return None

    response.raise_for_status()

    results = response.json().get("results", [])

    if not results:
        return None

    print(f"Tavily search SUCCESS: {len(results)} results")

    formatted = []

    for item in results:
        title = item.get("title", "")
        content = item.get("content", "")
        url = item.get("url", "")
        published = item.get("published_date", "")

        formatted.append(
            f"TITLE: {title}\n"
            f"DATE: {published}\n"
            f"CONTENT: {content}\n"
            f"SOURCE: {url}"
        )

    return "\n\n".join(formatted)


def ask_with_web(message):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    search_query = (
        f"{message}\n"
        f"Today's date is {today}. "
        f"Prioritize recent and verifiable information."
    )

    search_results = search_tavily(search_query)

    if not search_results:
        return None

    prompt = f"""
User ka question:

{message}

Current date:
{today}

Neeche Tavily web-search results hain:

{search_results}

IMPORTANT:
- Sirf provided search results ke basis par answer do.
- Future-dated information ko current news mat bolo.
- Agar source ki date unclear hai, clearly mention karo.
- Conflicting dates/information ho to usko hide mat karo.
- Information invent mat karo.
- Answer natural Hinglish me do.
- End me "Sources" section do.
- Sources me maximum 3 important source URLs include karo.
"""

    answer = ask_openrouter(prompt)

    return answer


def ask_local_ai(user_message):
    message = user_message.strip()

    if not message:
        return "😅 Kuchh likho bhai."

    lower = message.lower()

    web_words = [
        "latest",
        "today",
        "news",
        "current",
        "search",
        "internet",
        "web",
        "recent",
        "update",
        "aaj",
        "abhi",
        "taza",
        "taaza",
        "haal",
        "khabar",
    ]

    needs_web = any(word in lower for word in web_words)

    # 🔎 Current/web questions → Tavily + OpenRouter
    if needs_web and TAVILY_API_KEY:
        try:
            result = ask_with_web(message)

            if result:
                return result

        except Exception as e:
            print("Tavily/Web error:", e)

    # 🤖 Normal AI → OpenRouter
    try:
        result = ask_openrouter(message)

        if result:
            return result

    except requests.HTTPError as e:
        print("OpenRouter HTTP error:", e)

    except Exception as e:
        print("OpenRouter error:", e)

    # 🧠 Optional Ollama fallback
    if OLLAMA_URL:
        try:
            response = requests.post(
                OLLAMA_URL,
                headers={
                    "Content-Type": "application/json",
                },
                json={
                    "model": "llama3.2",
                    "prompt": f"{SYSTEM_PROMPT}\n\nUser: {message}",
                    "stream": False,
                },
                timeout=180,
            )

            response.raise_for_status()

            result = response.json().get("response", "").strip()

            if result:
                return result

        except Exception as e:
            print("Ollama fallback error:", e)

    return "😔 Nova abhi response nahi de pa rahi hai. Thodi der baad try karo."