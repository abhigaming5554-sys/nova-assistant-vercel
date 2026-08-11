from pathlib import Path
from app.modules.screen_reader import read_screen_text
from app.modules.local_ai import ask_local_ai

PROJECT_PATH = Path(r"C:\Users\lenovo\astra-assistant")

def auto_fix_from_screen():
    # 📸 Screen ka text padho
    screen_text = read_screen_text()

    prompt = f"""
    Neeche VS Code ya terminal ka error hai:

    {screen_text}

    Tum ek expert Python developer ho.

    1. Error identify karo
    2. Kaunsi file me problem ho sakti hai batao
    3. Exact corrected code do
    4. Hinglish me short explanation do
    """

    result = ask_local_ai(prompt)

    return result