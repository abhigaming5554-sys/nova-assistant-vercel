from pathlib import Path
from app.modules.local_ai import ask_local_ai
from app.modules.project_reader import read_project_context

PROJECT_PATH = r"C:\Users\lenovo\ai-story-studio"

def generate_homepage():
    context = read_project_context(PROJECT_PATH)

    prompt = f"""
    Tum ek expert Next.js + Tailwind developer ho.

    Existing project context:
    {context}

    Ek modern AI startup homepage banao jisme ho:
    - Hero section
    - Features
    - AI Story Generator showcase
    - CTA section
    - Dark gradient design
    - Responsive Tailwind CSS

    Sirf complete TSX code do.
    """

    code = ask_local_ai(prompt)

    page_file = Path(PROJECT_PATH) / "app" / "page.tsx"

    page_file.write_text(code, encoding="utf-8")

    return str(page_file)