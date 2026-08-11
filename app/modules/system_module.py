import os
from app.core.speech_engine import speak

def open_chrome():
    speak("Chrome khol raha hoon")
    os.system("start chrome")

def open_vscode():
    speak("VS Code khol raha hoon")
    os.system(r'"C:\Users\lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe"')