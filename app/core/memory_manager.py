import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("app/data/memory/memory.json")

DEFAULT_MEMORY = {
    "owner": "Abhay",
    "current_project": "AI Story Studio",
    "last_task": "",
    "last_file": "",
    "pending_tasks": [],
    "conversation_notes": [],
    "updated_at": ""
}

def load_memory():
    if not MEMORY_FILE.exists():
        save_memory(DEFAULT_MEMORY)
        return DEFAULT_MEMORY

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return DEFAULT_MEMORY

def save_memory(data):
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def remember_task(task, file_name=""):
    memory = load_memory()

    memory["last_task"] = task

    if file_name:
        memory["last_file"] = file_name

    save_memory(memory)

def add_pending_task(task):
    memory = load_memory()

    if task not in memory["pending_tasks"]:
        memory["pending_tasks"].append(task)

    save_memory(memory)

def add_note(note):
    memory = load_memory()

    memory["conversation_notes"].append({
        "time": datetime.now().strftime("%H:%M"),
        "note": note
    })

    # Sirf last 20 notes rakho
    memory["conversation_notes"] = memory["conversation_notes"][-20:]

    save_memory(memory)