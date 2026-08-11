from app.modules.local_ai import ask_local_ai


def generate_video_script(topic: str):
    prompt = f"""
Topic: {topic}

Ek cinematic funny YouTube Shorts script banao Hinglish me.

Format exactly:

🎬 TITLE:

🎭 SCENE 1:

🎭 SCENE 2:

🎭 SCENE 3:

🎙️ VOICEOVER:

🖼️ THUMBNAIL PROMPT:

🎥 AI VIDEO PROMPT (9:16):
"""

    return ask_local_ai(prompt)