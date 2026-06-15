from pydub import AudioSegment
import json

with open("translated_segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["hi"]

for i in range(min(10, len(segments))):

    audio = AudioSegment.from_file(f"tts_audio/seg_{i}.mp3")

    actual = len(audio) / 1000

    target = (
        segments[i]["end"]
        - segments[i]["start"]
    )

    print(
        f"SEG {i}: "
        f"audio={actual:.2f}s "
        f"target={target:.2f}s"
    )