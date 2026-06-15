from gtts import gTTS
from pydub import AudioSegment
import json
import os
import time

print("MULTI-LANGUAGE TTS STARTED")

with open("translated_segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

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

def match_duration(audio, target_ms):
    if len(audio) < target_ms:
        audio += AudioSegment.silent(target_ms - len(audio))
    return audio

for LANG in languages:

    print(f"\nGenerating {LANG} audio...")

    segments = data[LANG]

    output_folder = f"tts_{LANG}"
    os.makedirs(output_folder, exist_ok=True)

    for i, seg in enumerate(segments):

        text = seg["text"].strip()

        duration_ms = int(
            (seg["end"] - seg["start"]) * 1000
        )

        temp = f"temp_{LANG}_{i}.mp3"

        success = False

        for attempt in range(3):

            try:

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

                if os.path.exists(temp):
                    os.remove(temp)

                print(f"✔ {LANG} segment {i}")

                success = True
                break

            except Exception as e:

                print(
                    f"Retry {attempt + 1}/3 "
                    f"for {LANG} segment {i}"
                )

                time.sleep(2)

        if not success:

            print(
                f"❌ {LANG} segment {i} "
                f"failed after 3 attempts"
            )

    print(f"✅ {LANG} COMPLETE")

print("\nALL 8 LANGUAGE TTS GENERATED")