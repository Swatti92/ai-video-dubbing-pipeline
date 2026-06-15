from pydub import AudioSegment
import json
import os

LANG = input("Language code: ").strip()

print("Building video for", LANG)

with open("segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

audio_folder = "tts_" + LANG

timeline_duration = int(segments[-1]["end"] * 1000) + 3000

final_audio = AudioSegment.silent(
    duration=timeline_duration
)

for i, seg in enumerate(segments):

    path = os.path.join(
        audio_folder,
        f"seg_{i}.mp3"
    )

    start = int(seg["start"] * 1000)

    if not os.path.exists(path):
        print("Missing", path)
        continue

    try:

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

        print("Placed seg", i)

    except Exception as e:

        print(
            "Error in segment",
            i,
            e
        )

audio_file = LANG + "_dubbed_audio.wav"

final_audio.export(
    audio_file,
    format="wav"
)

output_video = LANG + "_dubbed_video.mp4"

cmd = (
    f'ffmpeg -y '
    f'-i video_1.mp4 '
    f'-i "{audio_file}" '
    f'-c:v copy '
    f'-map 0:v:0 '
    f'-map 1:a:0 '
    f'"{output_video}"'
)

os.system(cmd)

print("Created", output_video)