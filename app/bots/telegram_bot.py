import os
import telebot
from dotenv import load_dotenv

from app.modules.local_ai import ask_local_ai

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_TELEGRAM_ID", "0"))

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "⛔ Access denied")
        return

    bot.reply_to(message, "🤖 Nova online hai 😄")


@bot.message_handler(func=lambda m: True)
def handle(message):
    if message.from_user.id != OWNER_ID:
        return

    user_text = message.text

    bot.reply_to(message, "🧠 Soch rahi hoon...")

    reply = ask_local_ai(user_text)

    bot.reply_to(message, reply)


def start_telegram_bot():
    print("📱 Nova Telegram Bot started")
    bot.infinity_polling(skip_pending=True)