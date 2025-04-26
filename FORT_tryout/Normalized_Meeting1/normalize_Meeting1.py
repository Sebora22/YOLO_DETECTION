import os
import csv
from PIL import Image

# === Paths ===
raw_csv = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1_dataset\Meeting1_dataset.csv"
image_dir = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1\Meeting1\images" # Where your original .jpg images are stored
normalized_csv = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Normalized_Meeting1\normalized_Meeting1.csv"

# === Read Raw CSV ===
with open(raw_csv, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# === Prepare New CSV Rows ===
normalized_rows = [['frame_id', 'class_id', 'x_center', 'y_center', 'width', 'height']]

for row in rows:
    frame_id = row['frame_id']
    image_name = frame_id  # already like '000001.jpg'
    image_path = os.path.join(image_dir, image_name)

    if not os.path.exists(image_path):
        print(f"Image {image_path} not found — skipping.")
        continue

    # Get image size
    with Image.open(image_path) as img:
        img_width, img_height = img.size

    # Parse bounding box values
    x = float(row['x'])
    y = float(row['y'])
    w = float(row['w'])
    h = float(row['h'])

    # Normalize
    x_center = x / img_width
    y_center = y / img_height
    w_norm = w / img_width
    h_norm = h / img_height

    # Append to CSV
    normalized_rows.append([
        frame_id, 0,  # class_id = 0 for person
        round(x_center, 6),
        round(y_center, 6),
        round(w_norm, 6),
        round(h_norm, 6)
    ])

# === Write to Normalized CSV ===
with open(normalized_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(normalized_rows)

print(f"✅ Normalized annotations saved to: {normalized_csv}")
