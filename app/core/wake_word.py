import speech_recognition as sr

def wait_for_wake_word():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                print("👂 Wake word ka wait kar rahi hoon...")
                audio = recognizer.listen(source, phrase_time_limit=3)

                text = recognizer.recognize_google(audio, language="hi-IN").lower()

                if (
                    "नोवा" in text
                    or "nova" in text
                    or "हे नोवा" in text
                    or "hey nova" in text
                ):
                    return True

            except:
                pass