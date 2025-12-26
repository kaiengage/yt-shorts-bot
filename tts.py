import random
from gtts import gTTS

VOICE_FILE = "voice.mp3"

SENTENCES = [
    "Sometimes silence is the best answer.",
    "Slow down. This moment matters.",
    "Nature always finds a way to inspire us.",
    "Breathe in peace, and let go of stress.",
    "Simple moments bring the greatest peace.",
    "Not everything needs to be rushed.",
]

def generate_voice(lang="en"):
    text = random.choice(SENTENCES)
    tts = gTTS(
        text=text,
        lang=lang,
        slow=False
    )
    tts.save(VOICE_FILE)
    return VOICE_FILE, text
