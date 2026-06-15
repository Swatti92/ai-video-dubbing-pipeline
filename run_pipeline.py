import os
import shutil
import sys

print("===================================")
print("AI VIDEO DUBBING PIPELINE")
print("===================================")

# Accept video from command line OR manual input
if len(sys.argv) > 1:
    video_name = sys.argv[1]
else:
    video_name = input(
        "Enter video filename: "
    ).strip()

if not os.path.exists(video_name):
    print("Video not found!")
    exit()

print("\nVideo found.")

# Store current video path for merge_all.py
with open(
    "current_video.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(video_name)

print("\nExtracting audio...")

cmd = f'ffmpeg -y -i "{video_name}" audio.wav'
os.system(cmd)

if not os.path.exists("audio.wav"):
    print("Audio extraction failed.")
    exit()

print("Audio extraction completed.")

print("\nStarting WhisperX transcription...")

os.system("python src/transcribe_whisperx.py")

if os.path.exists("segments_medium.json"):
    print("Transcription completed.")
else:
    print("Transcription failed.")
    exit()

shutil.copy(
    "segments_medium.json",
    "segments.json"
)

print("segments.json created.")

print("\nStarting translation...")

os.system("python src/translate_segments.py")

if os.path.exists("translated_segments.json"):
    print("Translation completed.")
else:
    print("Translation failed.")
    exit()

print("\nStarting TTS generation...")

os.system("python src/generate_tts_multi.py")

print("TTS generation completed.")

print("\nStarting video generation...")

os.system("python src/merge_all.py")

print("Video generation completed.")

print("\n===================================")
print("PIPELINE FINISHED SUCCESSFULLY")
print("===================================")
print("Audio files -> output_audio/")
print("Video files -> output_video/")