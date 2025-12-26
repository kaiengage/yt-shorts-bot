import os
from telegram.ext import Updater, CommandHandler
from pixabay import get_video
from video_utils import download_video, cut_video

TOKEN = os.environ.get("TELEGRAM_TOKEN")

# ======================
# COMMAND HANDLERS
# ======================

def start(update, context):
    update.message.reply_text(
        "✅ Bot aktif!\n\n"
        "Perintah tersedia:\n"
        "/status - cek status bot\n"
        "/testvideo - tes ambil video Pixabay\n"
        "/testcut - download & potong video 20–30 detik"
    )

def status(update, context):
    update.message.reply_text("🤖 Bot berjalan normal.")

def testvideo(update, context):
    update.message.reply_text("🔍 Mencari video dari Pixabay...")

    result = get_video()
    if not result:
        update.message.reply_text("❌ Video tidak ditemukan")
        return

    url, keyword = result
    update.message.reply_text(
        f"🎥 Video ditemukan\n"
        f"Tema: {keyword}\n"
        f"{url}"
    )

def testcut(update, context):
    update.message.reply_text("⏳ Mengambil & memproses video...")

    result = get_video()
    if not result:
        update.message.reply_text("❌ Gagal ambil video dari Pixabay")
        return

    url, keyword = result

    try:
        download_video(url)
        cut_video()
    except Exception as e:
        update.message.reply_text(f"❌ Error saat proses video:\n{e}")
        return

    update.message.reply_text(
        f"✅ Video berhasil diproses!\n"
        f"Tema: {keyword}\n"
        f"Durasi: 20–30 detik\n"
        f"Format: YouTube Shorts"
    )

# ======================
# MAIN
# ======================

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("testvideo", testvideo))
    dp.add_handler(CommandHandler("testcut", testcut))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
