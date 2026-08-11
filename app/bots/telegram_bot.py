import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_TELEGRAM_ID", "0"))

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "⛔ Access denied")
        return

    bot.reply_to(
        message,
        "🤖 Nova Railway par successfully online hai 😄🔥"
    )


@bot.message_handler(func=lambda m: True)
def handle(message):
    if message.from_user.id != OWNER_ID:
        return

    text = message.text

    # Simple AI-style reply
    bot.reply_to(message, f"🧠 Nova: Tumne bola → {text}")


def start_telegram_bot():
    print("📱 Nova Telegram Bot started")
    bot.infinity_polling(skip_pending=True)