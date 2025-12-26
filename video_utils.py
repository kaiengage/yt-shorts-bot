import requests
import random
import subprocess
import os

TEMP_VIDEO = "temp_video.mp4"
CUT_VIDEO = "cut_video.mp4"

def download_video(url):
    r = requests.get(url, stream=True, timeout=60)
    with open(TEMP_VIDEO, "wb") as f:
        for chunk in r.iter_content(1024 * 1024):
            if chunk:
                f.write(chunk)

def cut_video(min_sec=20, max_sec=30):
    # ambil durasi video
    cmd_duration = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        TEMP_VIDEO
    ]
    duration = float(subprocess.check_output(cmd_duration).decode().strip())

    length = random.randint(min_sec, max_sec)
    start = 0 if duration <= length else random.uniform(0, duration - length)

    cmd_cut = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-i", TEMP_VIDEO,
        "-t", str(length),
        "-vf", "scale=1080:1920",
        "-r", "24",
        "-an",
        CUT_VIDEO
    ]

    subprocess.run(cmd_cut, check=True)
    return CUT_VIDEO
