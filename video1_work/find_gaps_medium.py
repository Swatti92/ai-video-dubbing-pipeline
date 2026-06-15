import json

with open("segments_medium.json", "r", encoding="utf-8") as f:
    data = json.load(f)

segments = data["segments"]

print("\n=== GAPS FOUND ===\n")

for i in range(len(segments)-1):

    current_end = segments[i]["end"]
    next_start = segments[i+1]["start"]

    gap = next_start - current_end

    if gap > 1:
        print(
            f"Between segment {i} and {i+1}"
        )
        print(
            f"Gap: {gap:.3f} sec"
        )
        print(
            f"Time: {current_end:.3f} -> {next_start:.3f}"
        )
        print("-"*50)