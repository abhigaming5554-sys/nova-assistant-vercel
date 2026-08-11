import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=6
            )

        text = recognizer.recognize_google(audio, language="hi-IN")

        print(f"🗣️ You: {text}")

        return text.lower()

    except:
        return ""