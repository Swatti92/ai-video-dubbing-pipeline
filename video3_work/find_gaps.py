import json

with open("segments_medium.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

print("\n=== GAPS FOUND ===\n")

for i in range(len(segments) - 1):

    gap = segments[i + 1]["start"] - segments[i]["end"]

    if gap > 1.0:

        print(
            f"Between {i} and {i+1} | Gap = {gap:.3f}s"
        )