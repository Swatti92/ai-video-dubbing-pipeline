import os

video_list = [
    "video1_work/video_1.mp4",
    "video2_work/video_2.mp4.webm",
    "video3_work/video_3.mp4"
]

for video in video_list:

    print("\n================================")
    print("PROCESSING:", video)
    print("================================\n")

    os.system(
        f'python run_pipeline.py "{video}"'
    )

print("\nALL VIDEOS COMPLETED")