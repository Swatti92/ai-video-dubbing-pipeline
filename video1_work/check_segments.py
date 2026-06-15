import json

with open("segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"] if "segments" in data else data

print("\n===== SEGMENT CHECK (1 TO 5) =====\n")

for i in range(1, 6):
    print(f"SEGMENT {i}:")
    print(segments[i]["text"])
    print("---------------------------------\n")