import json
import os
import telebot
from http.server import BaseHTTPRequestHandler

from app.modules.local_ai import ask_local_ai


TOKEN = os.getenv("BOT_TOKEN")

PRANK_URL = "https://prank.abhayrathore6306.workers.dev/"

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 Nova online hai 😄🔥\n\n"
        "Welcome! Ab tum Nova ko use kar sakte ho.\n\n"
        "🌐 Prank Website:\n"
        f"{PRANK_URL}\n\n"
        "💬 Normal message bhejo aur Nova se baat karo."
    )


@bot.message_handler(commands=["link"])
def send_link(message):
    bot.reply_to(
        message,
        "🌐 Nova Prank Website 😈🔥\n\n"
        f"{PRANK_URL}"
    )


@bot.message_handler(commands=["memory"])
def memory(message):
    bot.reply_to(
        message,
        "🔒 Memory command public users ke liye available nahi hai."
    )


@bot.message_handler(func=lambda m: True)
def handle_message(message):

    text = (message.text or "").strip()

    if not text:
        return

    # Abhi Vercel version mein video generation disabled hai.
    if text.lower().startswith("/video"):
        bot.reply_to(
            message,
            "🎬 Video generation abhi temporarily available nahi hai.\n"
            "Ye feature next step mein add karenge. 😄"
        )
        return

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

        print("AI error:", e)

        bot.reply_to(
            message,
            "😔 Nova abhi response nahi de pa rahi hai. "
            "Thodi der baad try karo."
        )


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        try:

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            update_data = json.loads(
                body.decode("utf-8")
            )

            update = telebot.types.Update.de_json(
                json.dumps(update_data)
            )

            bot.process_new_updates([update])

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                b'{"ok":true}'
            )

        except Exception as e:

            print("Webhook error:", e)

            self.send_response(500)
            self.send_header(
                "Content-Type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                b'{"ok":false}'
            )

    def do_GET(self):

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/plain"
        )
        self.end_headers()

        self.wfile.write(
            b"Nova Telegram Webhook is running."
        )