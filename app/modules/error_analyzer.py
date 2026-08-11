from app.modules.local_ai import ask_local_ai

def analyze_error(screen_text):
    prompt = f"""
    Tum ek expert software engineer ho.

    Neeche VS Code ya terminal ka text hai:

    {screen_text}

    Is error ko simple Hinglish me samjhao:
    - Problem kya hai
    - Kaunsi file me issue hai
    - Exact fix kya karna chahiye
    - Agar possible ho to corrected code bhi do
    """

    return ask_local_ai(prompt)