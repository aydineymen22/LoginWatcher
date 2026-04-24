import cv2
import time
from datetime import datetime
import os

SAVE_DIR = "captures"

def take_photo():
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print("[!] Camera failed to open")
        return None

    for _ in range(5):
        cap.read()
        time.sleep(0.05)

    ret, frame = cap.read()
    
    if ret:
        filename = datetime.now().strftime("intruder_%Y%m%d_%H%M%S.jpg")
        path = os.path.join(SAVE_DIR, filename)
        cv2.imwrite(path, frame)
        print(f"[📸] Photo saved: {path}")
    else:
        print("[!] Failed to capture frame")
        path = None

    cap.release()
    return path