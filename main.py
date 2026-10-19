import time
import cv2
import numpy as np
import mss

FPS = 20.0
OUTPUT = "recording.mp4"

with mss.mss() as sct:
    monitor = sct.monitors[1]  # main monitor
    width, height = monitor["width"], monitor["height"]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(OUTPUT, fourcc, FPS, (width, height))

    print("recording has started. to stop click Ctrl+C")
    frame_time = 1 / FPS

    try:
        while True:
            start = time.time()
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            out.write(frame)

            elapsed = time.time() - start
            if elapsed < frame_time:
                time.sleep(frame_time - elapsed)
    except KeyboardInterrupt:
        pass
    finally:
        out.release()
        print(f"saved: {OUTPUT}")
