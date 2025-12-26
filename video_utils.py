import subprocess

def cut_video(input_file, start_time=0, duration=25, output_file="cut_video.mp4"):
    """
    Potong video dengan durasi tertentu menggunakan FFmpeg
    """
    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-ss", str(start_time),
        "-t", str(duration),
        "-c", "copy",
        output_file
    ]
    subprocess.run(cmd, check=True)
    return output_file

def merge_video_audio(video_file, audio_file, output_file="final_short.mp4"):
    """
    Gabungkan video + audio menjadi satu file mp4
    """
    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_file
    ]
    subprocess.run(cmd, check=True)
    return output_file
