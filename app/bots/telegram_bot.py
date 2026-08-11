import os
import telebot
from dotenv import load_dotenv

from app.modules.local_ai import ask_local_ai
from app.core.command_router import route

# .env load karo
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_TELEGRAM_ID"))

bot = telebot.TeleBot(TOKEN)


def is_owner(message):
    return message.from_user.id == OWNER_ID


@bot.message_handler(commands=['start'])
def start(message):
    if not is_owner(message):
        bot.reply_to(message, "⛔ Access denied")
        return

    bot.reply_to(
        message,
        "🤖 Nova online hai 😄\nRemote AI assistant ready!"
    )


@bot.message_handler(func=lambda m: True)
def handle(message):
    if not is_owner(message):
        return

    text = message.text.lower()

    # Computer commands execute karo
    route(text)

    # AI reply generate karo
    reply = ask_local_ai(text)

    bot.reply_to(message, reply)


def start_telegram_bot():
    print("📱 Nova Telegram Bot started")
    bot.infinity_polling(skip_pending=True)