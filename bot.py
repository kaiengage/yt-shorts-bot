import os
from telegram.ext import Updater, CommandHandler
from pixabay import get_video
from video_utils import download_video, cut_video
from tts import generate_voice

TOKEN = os.environ.get("TELEGRAM_TOKEN")

def testtts(update, context):
    voice, text = generate_voice(lang="en")
    update.message.reply_text(f"🔊 Voice dibuat:\n{text}")

def start(update, context):
    update.message.reply_text(
        "🤖 Bot aktif\n"
        "/testcut - ambil & potong video Shorts"
    )

def testcut(update, context):
    update.message.reply_text("⏳ Proses video...")

    result = get_video()
    if not result:
        update.message.reply_text("❌ Gagal ambil video")
        return

    url, keyword = result

    try:
        download_video(url)
        cut_video()
    except Exception as e:
        update.message.reply_text(f"❌ Error:\n{e}")
        return

    update.message.reply_text(
        f"✅ Video siap\nTema: {keyword}\nDurasi: 20–30 detik"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("testcut", testcut))
    dp.add_handler(CommandHandler("testtts", testtts))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
