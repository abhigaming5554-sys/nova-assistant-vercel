from pathlib import Path
from app.modules.local_ai import ask_local_ai

PROJECT_PATH = Path(r"C:\Users\lenovo\ai-story-studio")

def create_modern_homepage():
    prompt = """
    Next.js 16 + Tailwind CSS ke liye ek premium AI SaaS homepage banao.

    Include:
    - Hero section
    - Gradient background
    - AI Story Studio branding
    - Features grid
    - Testimonials
    - CTA button
    - Fully responsive design

    Sirf complete page.tsx code do.
    """

    code = ask_local_ai(prompt)

    page_file = PROJECT_PATH / "app" / "page.tsx"

    page_file.write_text(code, encoding="utf-8")

    return page_file