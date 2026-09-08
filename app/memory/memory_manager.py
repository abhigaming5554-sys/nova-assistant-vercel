import json
import os


MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "memory.json"
)


DEFAULT_MEMORY = {
    "current_project": "Nova Telegram AI Bot",
    "last_task": "",
    "last_file": "",
    "pending_tasks": []
}


def load_memory():
    """Memory file read karta hai."""
    if not os.path.exists(MEMORY_FILE):
        save_memory(DEFAULT_MEMORY.copy())
        return DEFAULT_MEMORY.copy()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Missing fields automatically add kar do
        memory = DEFAULT_MEMORY.copy()
        memory.update(data)

        return memory

    except (json.JSONDecodeError, OSError) as e:
        print(f"Memory read error: {e}")
        return DEFAULT_MEMORY.copy()


def save_memory(memory):
    """Memory ko JSON file me save karta hai."""
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(
                memory,
                file,
                indent=2,
                ensure_ascii=False
            )

        return True

    except OSError as e:
        print(f"Memory save error: {e}")
        return False


def update_memory(
    current_project=None,
    last_task=None,
    last_file=None,
    pending_tasks=None
):
    """Nova ki memory update karta hai."""

    memory = load_memory()

    if current_project is not None:
        memory["current_project"] = current_project

    if last_task is not None:
        memory["last_task"] = last_task

    if last_file is not None:
        memory["last_file"] = last_file

    if pending_tasks is not None:
        memory["pending_tasks"] = pending_tasks

    save_memory(memory)

    return memory


def add_pending_task(task):
    """Naya pending task add karta hai."""

    memory = load_memory()

    if task not in memory["pending_tasks"]:
        memory["pending_tasks"].append(task)

    save_memory(memory)

    return memory


def remove_pending_task(task):
    """Completed task ko pending list se remove karta hai."""

    memory = load_memory()

    if task in memory["pending_tasks"]:
        memory["pending_tasks"].remove(task)

    save_memory(memory)

    return memory


def get_memory():
    """Current complete memory return karta hai."""
    return load_memory()


def clear_memory():
    """Memory reset karta hai."""

    memory = DEFAULT_MEMORY.copy()
    save_memory(memory)

    return memory