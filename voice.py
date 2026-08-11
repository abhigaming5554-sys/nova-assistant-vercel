import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Bolo...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=6
            )

        print("🔍 Processing...")

        text = recognizer.recognize_google(audio, language="hi-IN")

        print(f"✅ You said: {text}")
        return text.lower()

    except sr.WaitTimeoutError:
        print("⏰ Timeout - kuch nahi bola gaya")
        return ""

    except sr.UnknownValueError:
        print("❌ Samajh nahi aaya")
        return ""

    except Exception as e:
        print(f"⚠️ Voice error: {e}")
        return ""