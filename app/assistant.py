from app.core.voice_engine import listen
from app.core.speech_engine import speak
from app.core.command_router import route
from app.core.wake_word import wait_for_wake_word
from app.core.memory_manager import load_memory
from app.core.memory_manager import remember_task

remember_task(
    "AI Story Studio homepage redesign",
    "app/page.tsx"
)


def start_assistant():
    memory = load_memory()

    # Startup greeting
    if memory["last_task"]:
        speak(
            f"Hey Abhay 😄 last time hum {memory['last_task']} par kaam kar rahe the. Continue karein?"
        )
    else:
        speak("Hey Abhay 😄 Nova online hai")

    # Main assistant loop
    while True:
        # Wake word ka wait
        wait_for_wake_word()

        speak("हाँ Abhay 😄 बोलो, क्या करना है?")

        command = listen()

        if not command:
            continue

        if "बंद हो जाओ" in command or "band ho jao" in command:
            speak("ठीक है 😄 मैं बंद हो रही हूँ।")
            break

        # Command execute karo
        route(command)