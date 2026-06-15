import json
from pydub import AudioSegment
import os

segments_file = "segments.json"
audio_dir = "output_audio"

with open(segments_file, "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"] if isinstance(data, dict) else data

final_audio = AudioSegment.silent(duration=0)

print("Starting sync process...")

for i, seg in enumerate(segments):
    start = int(seg["start"] * 1000)
    end = int(seg["end"] * 1000)

    duration = end - start

    # Example: English Hindi folder (you can change language here)
    audio_path = f"{audio_dir}/hi/seg_{i}.mp3"

    if not os.path.exists(audio_path):
        print(f"Missing: {audio_path}")
        continue

    clip = AudioSegment.from_file(audio_path)

    # Adjust speed by padding or trimming
    if len(clip) < duration:
        silence = AudioSegment.silent(duration=(duration - len(clip)))
        clip = clip + silence
    else:
        clip = clip[:duration]

    final_audio += clip

output_file = "final_dubbed_audio.wav"
final_audio.export(output_file, format="wav")

print("DONE ✔ Synced audio created:", output_file)