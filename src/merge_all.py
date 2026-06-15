from pydub import AudioSegment
import json
import os

VIDEO_FILE = "current_video.txt"

if not os.path.exists(VIDEO_FILE):
    print("current_video.txt not found")
    exit()

with open(VIDEO_FILE, "r", encoding="utf-8") as f:
    video_path = f.read().strip()

languages = [
    "hi",
    "te",
    "ta",
    "bn",
    "mr",
    "gu",
    "kn",
    "ml"
]

with open("segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

os.makedirs("output_audio", exist_ok=True)
os.makedirs("output_video", exist_ok=True)

for LANG in languages:

    print("\nBuilding", LANG)

    audio_folder = f"tts_{LANG}"

    timeline_duration = (
        int(segments[-1]["end"] * 1000)
        + 3000
    )

    final_audio = AudioSegment.silent(
        duration=timeline_duration
    )

    for i, seg in enumerate(segments):

        path = os.path.join(
            audio_folder,
            f"seg_{i}.mp3"
        )

        if not os.path.exists(path):
            continue

        start = int(seg["start"] * 1000)

        audio = AudioSegment.from_file(path)

        end_pos = start + len(audio)

        if end_pos > len(final_audio):

            extra = end_pos - len(final_audio)

            final_audio += AudioSegment.silent(
                duration=extra
            )

        final_audio = (
            final_audio[:start]
            + audio
            + final_audio[end_pos:]
        )

    audio_file = (
        f"output_audio/{LANG}_dubbed_audio.wav"
    )

    final_audio.export(
        audio_file,
        format="wav"
    )

    output_video = (
        f"output_video/{LANG}_dubbed_video.mp4"
    )

    cmd = (
        f'ffmpeg -y '
        f'-i "{video_path}" '
        f'-i "{audio_file}" '
        f'-c:v copy '
        f'-map 0:v:0 '
        f'-map 1:a:0 '
        f'"{output_video}"'
    )

    os.system(cmd)

    print("Created", output_video)

print("\nALL 8 VIDEOS CREATED")