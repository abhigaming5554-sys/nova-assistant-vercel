from pathlib import Path
from app.modules.local_ai import ask_local_ai

PROJECT_PATH = Path(r"C:\Users\lenovo\ai-story-studio")

def update_homepage_from_voice(instruction):
    page_file = PROJECT_PATH / "app" / "page.tsx"

    current = page_file.read_text(encoding="utf-8")

    prompt = f"""
    Existing page.tsx:
    {current[:4000]}

    User instruction:
    {instruction}

    Existing design ko improve karo aur complete updated TSX code do.
    """

    updated_code = ask_local_ai(prompt)

    page_file.write_text(updated_code, encoding="utf-8")

    return "Homepage update ho gaya 😎"