import asyncio
import edge_tts
import pygame
import tempfile
import os
import time

# 🌸 Soft Hindi Female Voice
VOICE = "hi-IN-MadhurNeural"

pygame.mixer.init()

async def _speak_async(text):
    # Temporary mp3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        temp_file = f.name

    # 🎙️ Natural Hindi voice settings
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="-10%",
        pitch="+14Hz",
        volume="+10%"
    )

    await communicate.save(temp_file)

    # Play audio
    pygame.mixer.music.stop()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    time.sleep(0.2)

    # Delete temp file safely
    try:
        os.remove(temp_file)
    except:
        pass


def speak(text):
    print(f"🤖 Nova: {text}")

    try:
        asyncio.run(_speak_async(text))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(_speak_async(text))
        loop.close()