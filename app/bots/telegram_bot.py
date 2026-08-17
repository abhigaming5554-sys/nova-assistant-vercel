import os
import telebot
from dotenv import load_dotenv

from app.modules.local_ai import ask_local_ai
from app.video.video_generator import create_video

from app.memory.memory_manager import (
    get_memory,
    update_memory,
    add_pending_task,
    remove_pending_task,
)

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

    # 🧠 Memory command
    @bot.message_handler(commands=["memory"])
    def show_memory(message):
        if message.from_user.id != OWNER_ID:
            return

        memory = get_memory()

        pending = memory.get("pending_tasks", [])

        if pending:
            tasks = "\n".join(f"• {task}" for task in pending)
        else:
            tasks = "• Koi pending task nahi hai."

        reply = (
            "🧠 Nova Memory\n\n"
            f"📂 Project: {memory.get('current_project', '')}\n"
            f"🎯 Last task: {memory.get('last_task', '')}\n"
            f"📄 Last file: {memory.get('last_file', '')}\n\n"
            f"⏳ Pending tasks:\n{tasks}"
        )

        bot.reply_to(message, reply)
def show_memory(message):
    if message.from_user.id != OWNER_ID:
        return

    memory = get_memory()

    pending = memory.get("pending_tasks", [])

    if pending:
        tasks = "\n".join(f"• {task}" for task in pending)
    else:
        tasks = "• Koi pending task nahi hai."

    reply = (
        "🧠 Nova Memory\n\n"
        f"📂 Project: {memory.get('current_project', '')}\n"
        f"🎯 Last task: {memory.get('last_task', '')}\n"
        f"📄 Last file: {memory.get('last_file', '')}\n\n"
        f"⏳ Pending tasks:\n{tasks}"
    )

    bot.reply_to(message, reply)


# 💬 Main message handler
@bot.message_handler(func=lambda m: True)
def handle(message):
    if message.from_user.id != OWNER_ID:
        return

    text = message.text.strip()

    # 🎬 Custom cinematic video command
    if text.lower().startswith("/video "):
        scene_data = text[7:]

        bot.reply_to(
            message,
            "🎬 Nova tumhara cinematic scene video bana rahi hai... 😄🔥"
        )

        try:
            # Format: title###image_prompt###dialogue
            parts = scene_data.split("###")

            if len(parts) < 3:
                bot.reply_to(
                    message,
                    "❌ Format galat hai bhai 😅\n\nUse:\n/video Scene Title###Image Prompt###Dialogue"
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