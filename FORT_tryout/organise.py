import os
import shutil
import pandas as pd

# === CONFIGURATION ===
base_dir = r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1"
images_dir = os.path.join(base_dir, r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Meeting1\Meeting1\images")
csv_path = os.path.join(base_dir, r"C:\Users\Stagiaire\Desktop\FORT-tryout\FORT_tryout\Normalized_Meeting1\normalized_Meeting1.csv")  # Your normalized CSV

# Output directories
output_images = {
    'train': os.path.join(images_dir, 'train'),
    'val': os.path.join(images_dir, 'val')
}
output_labels = {
    'train': os.path.join(base_dir, 'labels/train'),
    'val': os.path.join(base_dir, 'labels/val')
}

# Create all necessary folders
for folder in list(output_images.values()) + list(output_labels.values()):
    os.makedirs(folder, exist_ok=True)

# === STEP 1: Split images by frame number
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

train_frames = set()
val_frames = set()

for filename in image_files:
    try:
        frame_number = int(os.path.splitext(filename)[0])
    except ValueError:
        print(f"⚠️ Skipping file that doesn't match frame pattern: {filename}")
        continue

    subset = 'train' if frame_number <= 600 else 'val'
    frame_padded = f"{frame_number:06d}.jpg"

    # Copy image to train/val folder
    shutil.copy(os.path.join(images_dir, filename), os.path.join(output_images[subset], filename))

    # Track which frames go where
    if subset == 'train':
        train_frames.add(frame_padded)
    else:
        val_frames.add(frame_padded)

# === STEP 2: Load normalized CSV
df = pd.read_csv(csv_path)

# === STEP 3: Generate YOLO-format .txt labels per image
for subset, frame_set in [('train', train_frames), ('val', val_frames)]:
    grouped = df[df['frame_id'].isin(frame_set)].groupby('frame_id')
    for frame_id, group in grouped:
        txt_name = frame_id.replace('.jpg', '.txt')
        label_path = os.path.join(output_labels[subset], txt_name)

        with open(label_path, 'w') as f:
            for _, row in group.iterrows():
                yolo_line = f"{int(row['class_id'])} {row['x_center']} {row['y_center']} {row['width']} {row['height']}"
                f.write(yolo_line + '\n')

print("✅ Split complete! Images and YOLO .txt labels are ready for training.")