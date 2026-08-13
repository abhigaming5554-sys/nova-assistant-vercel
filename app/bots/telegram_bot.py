import os
import telebot
from dotenv import load_dotenv

from app.modules.local_ai import ask_local_ai
from app.video.video_generator import create_video

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_TELEGRAM_ID", "0"))

bot = telebot.TeleBot(TOKEN)


# 🚀 Start command
@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "⛔ Access denied")
        return

    bot.reply_to(message, "🤖 Nova online hai 😄🔥")


# 💬 Main message handler
@bot.message_handler(func=lambda m: True)
def handle(message):
    if message.from_user.id != OWNER_ID:
        return

    text = message.text.strip()

    # 🎬 Video command
    if text.lower().startswith("/video "):
        topic = text[7:]

        bot.reply_to(
            message,
            "🎬 Nova tumhare liye video bana rahi hai... 😄🔥"
        )

        try:
            video_path = create_video(topic)

            with open(video_path, "rb") as video:
                bot.send_video(
                    message.chat.id,
                    video,
                    caption=f"🎬 {topic}"
                )

        except Exception as e:
            bot.reply_to(
                message,
                f"❌ Video generate nahi hua bhai: {e}"
            )

        return

    # 🤖 Normal AI chat
    bot.reply_to(message, "🤖 Nova soch rahi hai... 😄")

    reply = ask_local_ai(text)

    bot.reply_to(message, reply)


def start_telegram_bot():
    print("📱 Nova Bot started")

    try:
        bot.remove_webhook()
    except Exception as e:
        print("Webhook warning:", e)

    bot.infinity_polling(
        skip_pending=True,
        timeout=30,
        long_polling_timeout=30
    )