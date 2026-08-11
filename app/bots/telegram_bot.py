import os
import telebot
from dotenv import load_dotenv

from app.modules.local_ai import ask_local_ai
from app.video.script_generator import generate_video_script

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

    # 🎬 Video script command
    if text.lower().startswith("/video "):
        topic = text[7:]

        bot.reply_to(
            message,
            "🎬 Nova tumhare video ke liye cinematic script bana rahi hai... 😄🔥"
        )

        result = generate_video_script(topic)

        bot.reply_to(message, result)
        return

    # 🤖 Normal AI chat
    bot.reply_to(message, "🤖 Nova soch rahi hai... 😄")

    reply = ask_local_ai(text)

    bot.reply_to(message, reply)


def start_telegram_bot():
    print("📱 Nova Telegram Bot started")
    bot.infinity_polling(skip_pending=True)