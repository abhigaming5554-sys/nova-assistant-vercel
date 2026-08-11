from voice import listen
from speaker import speak
from commands import execute

speak("Astra assistant start ho gaya hai")

while True:
    try:
        text = listen()

        if not text:
            continue

        print(f"DEBUG: {text}")

        # Direct command execution
        execute(text)

    except KeyboardInterrupt:
        speak("Astra band ho raha hai")
        break

    except Exception as e:
        print(f"Error: {e}")