import requests
import random
import os
from moviepy.video.io.VideoFileClip 
import VideoFileClip

TEMP_VIDEO = "temp_video.mp4"
CUT_VIDEO = "cut_video.mp4"

def download_video(url):
    r = requests.get(url, stream=True, timeout=60)
    with open(TEMP_VIDEO, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

def cut_video(min_sec=20, max_sec=30):
    clip = VideoFileClip(TEMP_VIDEO)
    duration = clip.duration

    if duration <= max_sec:
        final = clip
    else:
        start = random.uniform(0, duration - max_sec)
        length = random.uniform(min_sec, max_sec)
        final = clip.subclip(start, start + length)

    final = final.resize((1080, 1920))
    final.write_videofile(
        CUT_VIDEO,
        fps=24,
        codec="libx264",
        audio=False,
        preset="ultrafast",
        verbose=False,
        logger=None
    )

    clip.close()
    final.close()

    return CUT_VIDEO
