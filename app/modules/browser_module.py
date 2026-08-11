import webbrowser
from app.core.speech_engine import speak

def open_youtube():
    speak("YouTube khol raha hoon")
    webbrowser.open("https://youtube.com")