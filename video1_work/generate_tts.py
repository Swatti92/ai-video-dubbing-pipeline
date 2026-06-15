import json
from gtts import gTTS
import os

print("🚀 TTS GENERATION STARTED")

# ---------------- LOAD TRANSLATED FILE ----------------
with open("translated_segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["hi"]

os.makedirs("tts_audio", exist_ok=True)

print(f"📊 Total segments: {len(segments)}")

# ---------------- GENERATE AUDIO ----------------
for i, seg in enumerate(segments):

    text = seg["text"].strip()

    if not text:
        print(f"⚠ Skipping empty segment {i}")
        continue

    try:
        tts = gTTS(text=text, lang="hi")
        output_file = f"tts_audio/seg_{i}.mp3"
        tts.save(output_file)

        print(f"✔ Generated seg_{i}")

    except Exception as e:
        print(f"❌ Error at segment {i}:", e)

print("\n✅ ALL TTS FILES CREATED")