import os
import random
import logging
import requests
from telegram.ext import Updater, CommandHandler
from tts import generate_voice
from video_utils import cut_video, merge_video_audio

# ===== LOGGING =====
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===== TELEGRAM TOKEN =====
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
PIXABAY_KEY = os.getenv("PIXABAY_KEY")  # API key Pixabay

if not TELEGRAM_TOKEN or not PIXABAY_KEY:
    raise ValueError("TELEGRAM_TOKEN atau PIXABAY_KEY belum diset!")

# ===== COMMANDS =====
def start(update, context):
    update.message.reply_text(
        "🤖 Bot aktif!\n\n"
        "Perintah:\n"
        "/short - buat short otomatis\n"
        "/ping - cek bot"
    )

def ping(update, context):
    update.message.reply_text("pong")

def download_pixabay_video(query="nature", filename="cut_video.mp4"):
    url = f"https://pixabay.com/api/videos/?key={PIXABAY_KEY}&q={query}&per_page=10"
    res = requests.get(url).json()
    hits = res.get("hits")
    if not hits:
        raise Exception("Video Pixabay tidak ditemukan")
    video_url = hits[random.randint(0, len(hits)-1)]["videos"]["medium"]["url"]
    r = requests.get(video_url, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(1024*1024):
            f.write(chunk)
    return filename

def create_short(update, context):
    try:
        update.message.reply_text("⬇️ Download video...")
        video_file = download_pixabay_video(query="nature")
        update.message.reply_text("✂️ Memotong durasi video...")
        cut_file = cut_video(video_file, duration=25)
        update.message.reply_text("🔊 Membuat suara TTS...")
        voice_file, _ = generate_voice()
        update.message.reply_text("🎬 Menggabungkan video + suara...")
        final_file = merge_video_audio(cut_file, voice_file)
        update.message.reply_text(f"✅ Short siap: {final_file}")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

# ===== MAIN =====
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("short", create_short))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
