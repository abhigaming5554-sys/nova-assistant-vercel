import pyautogui
import subprocess
import webbrowser
import time
from app.core.speech_engine import speak

pyautogui.FAILSAFE = True

def open_notepad():
    speak("नोटपैड खोल रही हूँ 😄")
    subprocess.Popen(["notepad.exe"])

def type_text(text):
    speak("ठीक है, मैं टाइप कर रही हूँ 😎")
    time.sleep(1)
    pyautogui.write(text, interval=0.03)

def open_folder(path):
    speak("फोल्डर खोल रही हूँ 📂")
    subprocess.Popen(["explorer", path])

def open_website(url):
    speak("वेबसाइट खोल रही हूँ 🌐")
    webbrowser.open(url)

def press_shortcut(keys):
    pyautogui.hotkey(*keys)