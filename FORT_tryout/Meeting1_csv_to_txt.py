import os
import csv

# === Path Setup ===
normalized_csv = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Normalized_Meeting1\normalized_Meeting1.csv"
output_label_dir = './FORT_tryout/Meeting1/labels/train'
os.makedirs(output_label_dir, exist_ok=True)

# === Read CSV
with open(normalized_csv, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# === Write individual .txt files
file_map = {}

for row in rows:
    filename = row['frame_id'].replace('.jpg', '')
    label_path = os.path.join(output_label_dir, filename + '.txt')

    yolo_line = f"{row['class_id']} {row['x_center']} {row['y_center']} {row['width']} {row['height']}"

    # Group annotations per file
    if label_path not in file_map:
        file_map[label_path] = []
    file_map[label_path].append(yolo_line)

# === Save to .txt files
for path, lines in file_map.items():
    with open(path, 'w') as f:
        f.write('\n'.join(lines))

print("✅ YOLO .txt annotation files generated!")
