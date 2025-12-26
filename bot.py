import os
from telegram.ext import Updater, CommandHandler
from pixabay import get_video
from video_utils import download_video, cut_video

TOKEN = os.environ.get("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text(
        "🤖 Bot aktif\n\n"
        "/status - cek status\n"
        "/testcut - ambil & potong video"
    )

def status(update, context):
    update.message.reply_text("✅ Bot berjalan normal")

def testcut(update, context):
    update.message.reply_text("⏳ Mengambil video dari Pixabay...")

    result = get_video()
    if not result:
        update.message.reply_text("❌ Video tidak ditemukan")
        return

    url, keyword = result

    try:
        download_video(url)
        cut_video()
    except Exception as e:
        update.message.reply_text(f"❌ Error:\n{e}")
        return

    update.message.reply_text(
        f"✅ Video siap\n"
        f"Tema: {keyword}\n"
        f"Durasi: 20–30 detik"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("testcut", testcut))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
