#— boilerplate to load each clip under data/<move>/, 
#run MediaPipe/OpenPose, and save per-video .npz landmark arrays.

# scripts/extract_keypoints.py

import os
import cv2
import numpy as np
import mediapipe as mp

# ==== CONFIG ====
MOVES = ["jugni", "dhamaal"]        # folder names under data/
DATA_DIR = os.path.join(os.path.dirname(__file__), "../videodata")
OUTPUT_EXT = ".npz"

# Initialize MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False,
                    model_complexity=1,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)

def process_video(in_path, out_path):
    cap = cv2.VideoCapture(in_path)
    keypoints = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR→RGB and run pose
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            # extract (x,y) for each of the 33 landmarks
            pts = []
            for lm in results.pose_landmarks.landmark:
                pts.extend([lm.x, lm.y])
            keypoints.append(pts)

    cap.release()

    if keypoints:
        arr = np.array(keypoints, dtype=np.float32)
        np.savez(out_path, data=arr)
        print(f"[✓] Saved {out_path}: shape {arr.shape}")
    else:
        print(f"[!] No landmarks detected in {in_path}")

if __name__ == "__main__":
    for move in MOVES:
        folder = os.path.join(DATA_DIR, move)
        if not os.path.isdir(folder):
            print(f"[!] Missing folder: {folder}")
            continue

        for fn in os.listdir(folder):
            if not fn.lower().endswith((".mp4", ".mov", ".avi")):
                continue
            in_path = os.path.join(folder, fn)
            base, _ = os.path.splitext(fn)
            out_path = os.path.join(folder, base + OUTPUT_EXT)
            process_video(in_path, out_path)