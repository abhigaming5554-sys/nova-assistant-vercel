import os
import telebot
from dotenv import load_dotenv

from app.modules.local_ai import ask_local_ai
from app.video.video_generator import create_video

from app.memory.memory_manager import (
    get_memory,
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# 🌐 Public prank website
PRANK_URL = "https://prank.abhayrathore6306.workers.dev/"

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN .env file me nahi mila!")

bot = telebot.TeleBot(TOKEN)


# 🚀 Start command
@bot.message_handler(commands=["start"])
def start(message):

    bot.reply_to(
        message,
        "🤖 Nova online hai 😄🔥\n\n"
        "Welcome! Ab tum Nova ko use kar sakte ho.\n\n"
        "🌐 Prank Website:\n"
        f"{PRANK_URL}\n\n"
        "💬 Normal message bhejo aur Nova se baat karo.\n"
        "🎬 Video banane ke liye /video command use karo."
    )


# 🌐 Website link command
@bot.message_handler(commands=["link"])
def send_link(message):

    bot.reply_to(
        message,
        "🌐 Nova Prank Website 😈🔥\n\n"
        f"{PRANK_URL}"
    )


# 🧠 Memory command
# Public bot hone ke baad memory ko intentionally private rakha gaya hai.
# Isliye /memory par public user ko sensitive data nahi milega.
@bot.message_handler(commands=["memory"])
def show_memory(message):

    bot.reply_to(
        message,
        "🔒 Memory command public users ke liye available nahi hai."
    )


# 💬 Main message handler
@bot.message_handler(func=lambda m: True)
def handle(message):

    text = (message.text or "").strip()

    if not text:
        return

    # 🎬 Custom cinematic video command
    if text.lower().startswith("/video "):

        scene_data = text[7:].strip()

        bot.reply_to(
            message,
            "🎬 Nova tumhara cinematic scene video bana rahi hai... 😄🔥"
        )

        try:

            # Format:
            # /video Scene Title###Image Prompt###Dialogue

            parts = scene_data.split("###")

            if len(parts) < 3:
                bot.reply_to(
                    message,
                    "❌ Format galat hai bhai 😅\n\n"
                    "Use:\n"
                    "/video Scene Title###Image Prompt###Dialogue"
                )
                return

            scene_title = parts[0].strip()
            image_prompt = parts[1].strip()
            dialogue = parts[2].strip()

            video_path = create_video(
                scene_title,
                image_prompt,
                dialogue
            )

            with open(video_path, "rb") as video:

                bot.send_video(
                    message.chat.id,
                    video,
                    caption=f"🎬 {scene_title}"
                )

        except Exception as e:

            bot.reply_to(
                message,
                f"❌ Video generate nahi hua bhai:\n{e}"
            )

        return


    # 🤖 Normal AI chat

    bot.reply_to(
        message,
        "🤖 Nova soch rahi hai... 😄"
    )

    try:

        reply = ask_local_ai(text)

        bot.reply_to(
            message,
            reply
        )

    except Exception as e:

        bot.reply_to(
            message,
            f"❌ Nova me error aa gaya:\n{e}"
        )


# ▶️ Start Telegram Bot
def start_telegram_bot():

    print("📱 Nova Public Bot started 🚀")

    try:
        bot.remove_webhook()

    except Exception as e:
        print("Webhook warning:", e)

    bot.infinity_polling(
        skip_pending=True,
        timeout=30,
        long_polling_timeout=30
    )