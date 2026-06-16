import json
import time
from deep_translator import GoogleTranslator

print("MULTI-LANGUAGE TRANSLATION STARTED")

with open("segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

print("Total segments:", len(segments))

languages = {
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "bn": "Bengali",
    "mr": "Marathi",
    "gu": "Gujarati",
    "kn": "Kannada",
    "ml": "Malayalam"
}

def is_valid(text):
    if not text:
        return False

    text = text.strip()

    if len(set(text.replace(" ", ""))) < 3:
        return False

    if len(text) < 3:
        return False

    return True

def translate_text(text, lang_code):
    for _ in range(3):
        try:
            translator = GoogleTranslator(
                source="en",
                target=lang_code
            )
            return translator.translate(text)

        except Exception:
            time.sleep(1)

    return text

all_translations = {}

for lang_code, lang_name in languages.items():

    print("\nTranslating to", lang_name)

    translated_segments = []

    for i, seg in enumerate(segments):

        text = seg["text"].strip()

        if not is_valid(text):
            continue

        translated_text = translate_text(
            text,
            lang_code
        )

        translated_segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": translated_text
        })

        if i % 5 == 0:
            print(
                f"{lang_code}: {i}/{len(segments)}"
            )

    all_translations[lang_code] = translated_segments

with open(
    "translated_segments.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        all_translations,
        f,
        indent=2,
        ensure_ascii=False
    )

print("\nALL 8 LANGUAGES TRANSLATED")
print("translated_segments.json created")