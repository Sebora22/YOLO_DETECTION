import os
import pandas as pd
from ultralytics import YOLO
from pathlib import Path

# --- CONFIG ---
MODEL_PATH = r"C:\Users\Stagiaire\Desktop\FORT-tryout\runs\detect\yolo_run2\weights\best.pt"
IMAGES_DIR = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1\Meeting1\images"     # 👈 put your test image folder here
OUTPUT_DIR = 'inference_outputs'       # will save results + images here
CSV_OUTPUT = 'detections.csv'

# --- LOAD MODEL ---
model = YOLO(MODEL_PATH)

# --- CREATE OUTPUT FOLDER ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- PROCESS ALL IMAGES ---
image_paths = list(Path(IMAGES_DIR).glob('*.jpg'))
all_detections = []

for img_path in image_paths:
    results = model(img_path, save=True, save_txt=False, conf=0.25, project=OUTPUT_DIR, name='results', exist_ok=True)

    for r in results:
        boxes = r.boxes
        for i in range(len(boxes)):
            cls = int(boxes.cls[i])
            conf = float(boxes.conf[i])
            xyxy = boxes.xyxy[i].tolist()  # [x1, y1, x2, y2]

            all_detections.append({
                'image': img_path.name,
                'class_id': cls,
                'confidence': round(conf, 3),
                'x1': round(xyxy[0], 1),
                'y1': round(xyxy[1], 1),
                'x2': round(xyxy[2], 1),
                'y2': round(xyxy[3], 1)
            })

# --- SAVE TO CSV ---
df = pd.DataFrame(all_detections)
df.to_csv(os.path.join(OUTPUT_DIR, CSV_OUTPUT), index=False)

print(f"[✅] Inference complete! Results saved to '{OUTPUT_DIR}/{CSV_OUTPUT}' and images saved with predictions.")
