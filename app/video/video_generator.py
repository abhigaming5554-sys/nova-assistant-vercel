import os
import re
import asyncio
import subprocess
import requests
from PIL import Image
import edge_tts

TEMP_DIR = "temp_video"
os.makedirs(TEMP_DIR, exist_ok=True)


def clean_filename(text):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", text)[:30]


def generate_image(prompt, path):
    url = f"https://image.pollinations.ai/prompt/{prompt}"

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    # Resize for Shorts
    img = Image.open(path).convert("RGB")
    img = img.resize((720, 1280))
    img.save(path)


async def generate_voice(text, output_file):
    communicate = edge_tts.Communicate(
        text,
        voice="hi-IN-SwaraNeural"
    )

    await communicate.save(output_file)


def create_video(scene_title, image_prompt, dialogue):
    safe_name = clean_filename(scene_title)

    image_path = os.path.join(TEMP_DIR, f"{safe_name}.png")
    audio_path = os.path.join(TEMP_DIR, f"{safe_name}.mp3")
    output_path = os.path.join(TEMP_DIR, f"{safe_name}.mp4")

    # 1️⃣ AI image generate
    generate_image(image_prompt, image_path)

    # 2️⃣ Voiceover generate
    asyncio.run(generate_voice(dialogue, audio_path))

    # 3️⃣ Video create
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-vf",
        "scale=720:1280,zoompan=z='min(zoom+0.0005,1.1)':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
        output_path
    ]

    subprocess.run(cmd, check=True)

    return output_path