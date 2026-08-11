from pathlib import Path
from app.modules.local_ai import ask_local_ai

PROJECT_PATH = Path(r"C:\Users\lenovo\ai-story-studio")

def find_relevant_file(task):
    files = [str(f.relative_to(PROJECT_PATH)) for f in PROJECT_PATH.rglob("*.tsx")]

    prompt = f"""
    Task: {task}

    Project files:
    {files}

    Is task ke liye sabse relevant file ka naam batao.
    Sirf file path return karo.
    """

    return ask_local_ai(prompt).strip()