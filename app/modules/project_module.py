import json
import os
import webbrowser
from pathlib import Path
from app.core.speech_engine import speak

PROJECTS_FILE = Path("app/memory/projects.json")

def load_projects():
    if PROJECTS_FILE.exists():
        with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def open_project(name):
    projects = load_projects()

    if name not in projects:
        speak(f"Project {name} registry me nahi mila")
        return

    path = projects[name]

    speak(f"{name} project khol raha hoon")
    os.system(f'code "{path}"')

def run_dev_server(name):
    projects = load_projects()

    if name not in projects:
        speak(f"Project {name} registry me nahi mila")
        return

    path = projects[name]

    speak("Development server start kar raha hoon")

    os.system(
        f'start powershell -NoExit -Command "cd \'{path}\'; npm run dev"'
    )

def open_localhost():
    speak("Localhost browser me khol raha hoon")
    webbrowser.open("http://localhost:3000")