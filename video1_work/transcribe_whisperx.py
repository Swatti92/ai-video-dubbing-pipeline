import whisperx
import json

audio_file = "audio.wav"
device = "cpu"

print("Loading WhisperX medium model...")

model = whisperx.load_model(
    "medium",
    device,
    language="en"
)

print("Transcribing audio...")

result = model.transcribe(
    audio_file,
    language="en"
)

print("Aligning words...")

model_a, metadata = whisperx.load_align_model(
    language_code="en",
    device=device
)

aligned = whisperx.align(
    result["segments"],
    model_a,
    metadata,
    audio_file,
    device
)

def clean_text(text):
    if not text:
        return ""

    text = text.strip()

    if len(text) > 20 and text.count("'") > 10:
        return ""

    return text

clean_segments = []

for seg in aligned["segments"]:

    text = clean_text(seg["text"])

    if text:
        clean_segments.append({
            "start": round(seg["start"], 3),
            "end": round(seg["end"], 3),
            "text": text
        })

with open(
    "segments_medium.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        {"segments": clean_segments},
        f,
        indent=2,
        ensure_ascii=False
    )

print("segments_medium.json created")
print("Total segments:", len(clean_segments))