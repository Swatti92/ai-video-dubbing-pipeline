import os
import json

with open("segments.json", "r", encoding="utf-8") as f:
    segments = json.load(f)["segments"]

missing = []

for i in range(len(segments)):
    path = f"tts_audio/seg_{i}.mp3"

    if not os.path.exists(path):
        missing.append(i)

print("TOTAL SEGMENTS:", len(segments))
print("MISSING AUDIO FILES:", missing)
print("COUNT MISSING:", len(missing))