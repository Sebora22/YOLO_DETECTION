import os
import shutil

MIXED_DIR   = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1\Meeting1"  # folder with both images and .txt
IMAGES_DIR  = os.path.join(MIXED_DIR, "images")
LABELS_DIR  = os.path.join(MIXED_DIR, "labels")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(LABELS_DIR, exist_ok=True)

# Move files to separate folders
for fname in os.listdir(MIXED_DIR):
    src = os.path.join(MIXED_DIR, fname)
    if os.path.isdir(src):
        continue
    ext = os.path.splitext(fname)[1].lower()
    if ext in {".jpg", ".jpeg", ".png", ".bmp"}:
        shutil.move(src, os.path.join(IMAGES_DIR, fname))
    elif ext == ".txt":
        shutil.move(src, os.path.join(LABELS_DIR, fname))

print(f"Images moved to: {IMAGES_DIR}")
print(f"Labels moved to: {LABELS_DIR}")
