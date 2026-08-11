from app.modules.system_module import open_chrome, open_vscode
from app.modules.browser_module import open_youtube
from app.modules.local_ai import ask_local_ai
from app.core.speech_engine import speak
from app.modules.computer_control import (
    open_notepad,
    type_text,
    open_folder,
    open_website,
)
from app.modules.code_agent import generate_homepage
from app.modules.screenshot_ai import take_screenshot
from app.core.speech_engine import speak
from app.modules.screen_reader import read_screen_text
from app.modules.error_analyzer import analyze_error
from app.modules.auto_coder import create_modern_homepage
from app.core.speech_engine import speak

from app.modules.voice_coder import update_homepage_from_voice
from app.modules.auto_fix_agent import auto_fix_from_screen
from app.modules.direct_writer import write_component
from app.core.memory_manager import (
    load_memory,
    add_pending_task,
    remember_task
)

def route(command):
    text = command.lower()

    # ---------------- REAL COMPUTER ACTIONS ----------------

    if "क्रोम" in text or "chrome" in text:
        speak("Done bhai 😎 Chrome khol diya.")
        open_chrome()
        return

    elif "वीएस कोड" in text or "vs code" in text:
        speak("VS Code ready hai 🚀 ab coding shuru karte hain.")
        open_vscode()
        return

    elif "यूट्यूब" in text or "youtube" in text:
        speak("YouTube khol diya 😄 dekhte hain aaj kya inspiration milti hai.")
        open_youtube()
        return

    elif "नोटपैड खोलो" in text or "notepad kholo" in text:
        open_notepad()
        return

    elif "डाउनलोड फोल्डर खोलो" in text or "downloads kholo" in text:
        open_folder(r"C:\Users\lenovo\Downloads")
        return

    elif "गूगल खोलो" in text or "google kholo" in text:
        open_website("https://google.com")
        return

    elif "मेरा नाम लिखो" in text or "mera naam likho" in text:
        type_text("Abhay Rathore")
        return

    elif "होमपेज बनाओ" in text or "homepage banao" in text:
        speak("ठीक है 😎 मैं नया homepage बना रही हूँ।")
        file_path = generate_homepage()
        speak("Homepage तैयार है और file में save कर दिया है।")
        print(f"Saved: {file_path}")
        return

    elif "स्क्रीनशॉट लो" in text or "screenshot lo" in text:
        path = take_screenshot()
        speak("स्क्रीनशॉट ले लिया 😄")
        print(path)
        return

    elif "स्क्रीन पढ़ो" in text or "screen padho" in text:
        speak("ठीक है 😄 स्क्रीन पढ़ रही हूँ।")
        content = read_screen_text()
        print(content)
        speak("मैंने स्क्रीन का टेक्स्ट पढ़ लिया।")
        return

    elif "एरर समझाओ" in text or "error samjhao" in text:
        speak("एक सेकंड 😄 एरर समझ रही हूँ।")
        content = read_screen_text()
        result = analyze_error(content)
        print(result)
        speak(result[:300])
        return

    elif "होमपेज बनाओ" in text or "homepage banao" in text:
        speak("ठीक है 😎 premium homepage बना रही हूँ।")
        file_path = create_modern_homepage()
        speak("होमपेज तैयार है और project में save कर दिया है।")
        print(file_path)
        return

    elif "होमपेज को मॉडर्न बनाओ" in text:
        speak("ठीक है 😎 homepage ko modern bana rahi hoon।")
        result = update_homepage_from_voice(
            "Make the homepage more modern with glassmorphism, gradient hero section, animated buttons and premium AI startup look."
        )
        speak(result)
        return

    elif "एरर फिक्स करो" in text or "error fix karo" in text:
        speak("एक सेकंड 😄 मैं स्क्रीन देखकर एरर समझ रही हूँ।")

        result = auto_fix_from_screen()

        print("\n🤖 AUTO FIX ANALYSIS:\n")
        print(result)

        speak("मैंने एरर का analysis कर लिया है। Terminal में पूरा solution दे दिया है 😎")
        return
    elif "हीरो सेक्शन बनाओ" in text:
        speak("ठीक है 😎 नया hero section बना रही हूँ।")

        path = write_component(
            "HeroSection",
            "Premium AI startup hero section with gradient background, glassmorphism, animated CTA buttons and responsive design"
        )

        speak("Hero section तैयार है और component में save कर दिया है 😄")
        print(path)
        return
    elif "याद रखो" in text or "yaad rakho" in text:
        note = text.replace("याद रखो", "").replace("yaad rakho", "").strip()

        remember_task(note)

        speak(f"ठीक है 😄 मैंने याद रख लिया: {note}")
        return

    elif "पेंडिंग टास्क जोड़ो" in text or "pending task jodo" in text:
        task = text.replace("पेंडिंग टास्क जोड़ो", "").replace("pending task jodo", "").strip()

        add_pending_task(task)

        speak(f"Done 😎 pending task list में जोड़ दिया: {task}")
        return

    elif "मेमोरी दिखाओ" in text or "memory dikhao" in text:
        memory = load_memory()

        print("\n🧠 ASTRA MEMORY:\n")
        print(memory)

        speak("मैंने memory terminal में दिखा दी है 😄")
        return

    

    # ---------------- SMART AI CONVERSATION ----------------

    reply = ask_local_ai(command)
    speak(reply)