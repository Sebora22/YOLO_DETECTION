import cv2
import os
import glob

image_folder = r"C:\Users\Stagiaire\Desktop\FORT-tryout\inference_outputs\results"
video_name = 'output_video.avi'

images = sorted(glob.glob(os.path.join(image_folder, '*.jpg')))
frame = cv2.imread(images[0])
height, width, _ = frame.shape

out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

for image in images:
    frame = cv2.imread(image)
    out.write(frame)

out.release()
print(f"[🎥] Video saved to: {video_name}")
