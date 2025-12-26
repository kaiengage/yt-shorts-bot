import os
import logging
from telegram.ext import Updater, CommandHandler
from tts import generate_voice

# ===== LOGGING =====
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# ===== COMMANDS =====
def start(update, context):
    update.message.reply_text(
        "🤖 Bot aktif!\n\n"
        "Perintah:\n"
        "/testcut - test video\n"
        "/testtts - test suara\n"
        "/ping - cek bot"
    )

def ping(update, context):
    update.message.reply_text("pong")

def testcut(update, context):
    update.message.reply_text("🎬 testcut masih aktif")

def testtts(update, context):
    voice, text = generate_voice(lang="en")
    update.message.reply_text(f"🔊 Voice dibuat:\n{text}")

# ===== MAIN =====
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN belum diset")

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("testcut", testcut))
    dp.add_handler(CommandHandler("testtts", testtts))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
