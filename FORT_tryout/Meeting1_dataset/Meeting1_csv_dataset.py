import os
import csv

# === Path Setup ===
annotation_dir = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1\Meeting1\labels"
output_csv = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1_dataset/Meeting1_dataset.csv"

# === CSV Header ===
rows = [['frame_id', 'class', 'x', 'y', 'w', 'h', 'R']]

# === Loop Through All Annotation Files ===
for filename in os.listdir(annotation_dir):
    if not filename.endswith('.txt'):
        continue

    base = os.path.splitext(filename)[0]
    txt_path = os.path.join(annotation_dir, filename)

    with open(txt_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 6:
                continue
            class_name, x, y, w, h, R = parts
            rows.append([base + '.jpg', class_name, x, y, w, h, R])

# === Write to CSV ===
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print(f"✅ Combined raw annotations saved to: {output_csv}")