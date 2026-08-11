from pathlib import Path
from app.modules.local_ai import ask_local_ai

PROJECT_PATH = Path(r"C:\Users\lenovo\ai-story-studio")

def write_component(component_name, instruction):
    prompt = f"""
    Next.js 16 + Tailwind CSS component banao.

    Component name: {component_name}
    Instruction: {instruction}

    Sirf complete TSX code do.
    """

    code = ask_local_ai(prompt)

    file_path = PROJECT_PATH / "components" / f"{component_name}.tsx"

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(code, encoding="utf-8")

    return str(file_path)