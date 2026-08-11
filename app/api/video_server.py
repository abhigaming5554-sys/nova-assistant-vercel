from fastapi import FastAPI
from app.modules.local_ai import ask_local_ai

app = FastAPI()

@app.get("/generate-video-script")
def generate_video_script(prompt: str):
    ai_prompt = f"""
Tum Nova ho aur cinematic YouTube Shorts script writer ho.

Topic: {prompt}

Ek short funny ya cinematic script banao Hinglish me.

Return format exactly:

TITLE:
SCENE 1:
SCENE 2:
SCENE 3:
SCENE 4:
VOICEOVER:
"""

    reply = ask_local_ai(ai_prompt)

    return {
        "prompt": prompt,
        "script": reply
    }