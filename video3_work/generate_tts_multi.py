from gtts import gTTS
from pydub import AudioSegment
import json
import os

LANG = input("Language code: ").strip()

with open("translated_segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data[LANG]

output_folder = f"tts_{LANG}"
os.makedirs(output_folder, exist_ok=True)

def match_duration(audio, target_ms):
    if len(audio) < target_ms:
        audio += AudioSegment.silent(target_ms - len(audio))
    return audio

for i, seg in enumerate(segments):

    text = seg["text"].strip()

    duration_ms = int(
        (seg["end"] - seg["start"]) * 1000
    )

    temp = f"temp_{i}.mp3"

    tts = gTTS(
        text=text,
        lang=LANG,
        slow=False
    )

    tts.save(temp)

    audio = AudioSegment.from_file(temp)

    audio = match_duration(
        audio,
        duration_ms
    )

    audio.export(
        f"{output_folder}/seg_{i}.mp3",
        format="mp3"
    )

    os.remove(temp)

    print(f"✔ {LANG} segment {i}")

print(f"\n✅ {LANG} TTS COMPLETE")