import os
import webbrowser
from speaker import speak

def execute(command):
    command = command.lower()

    # Chrome open
    if "क्रोम" in command or "chrome" in command:
        speak("Chrome khol raha hoon")
        os.system("start chrome")

    # VS Code open
    elif "वीएस कोड" in command or "vs code" in command:
        speak("VS Code khol raha hoon")
        os.system(r'"C:\Users\lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe"')

    # YouTube
    elif "यूट्यूब" in command or "youtube" in command:
        speak("YouTube khol raha hoon")
        webbrowser.open("https://youtube.com")

    # Google search
    elif "गूगल" in command or "google" in command:
        speak("Google khol raha hoon")
        webbrowser.open("https://google.com")

    # Hello
    elif "हेलो" in command or "hello" in command:
        speak("Hello Abhay, main Astra hoon")

    else:
        speak("Command mila, lekin abhi ye feature add nahi hua hai")