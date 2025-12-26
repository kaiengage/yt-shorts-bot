import os
import logging
from telegram.ext import Updater, CommandHandler
from tts import generate_voice

# ===== LOGGING =====
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===== BOT TOKEN =====
BOT_TOKEN = os.getenv("BOT_TOKEN")  # ambil dari GitHub Secrets

# ===== COMMANDS =====
def start(update, context):
    update.message.reply_text(
        "🤖 Bot aktif!\n\n"
        "Perintah:\n"
        "/testtts - test suara AI\n"
        "/ping - cek bot"
    )

def ping(update, context):
    update.message.reply_text("pong")

def testtts(update, context):
    voice, text = generate_voice(lang="en")
    update.message.reply_text(f"🔊 Voice dibuat:\n{text}")

# ===== MAIN =====
def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN belum di-set di environment!")

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("testtts", testtts))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
