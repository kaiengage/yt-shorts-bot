import os
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text(
        "✅ Bot aktif!\n\n"
        "Perintah tersedia:\n"
        "/status - cek status bot"
    )

def status(update, context):
    update.message.reply_text("🤖 Bot berjalan normal.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("status", status))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
