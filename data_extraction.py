import cv2
import os

# === Config ===
video_path = "input_video.mp4"   # Path to your video
project_name = "idcard"
output_dir = f"{project_name}_dataset"
frame_skip_interval = 5          # Extract 1 frame every 5
test_frame_gap = 15              # Ensure test frames are dissimilar
train_ratio = 0.7

# === Setup folder paths ===
image_train_dir = os.path.join(output_dir, "images/train")
image_test_dir = os.path.join(output_dir, "images/val")
label_train_dir = os.path.join(output_dir, "labels/train")
label_test_dir = os.path.join(output_dir, "labels/val")

for folder in [image_train_dir, image_test_dir, label_train_dir, label_test_dir]:
    os.makedirs(folder, exist_ok=True)

# === Extract frames ===
cap = cv2.VideoCapture(video_path)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

extracted_frames = []
frame_index = 0

print("[INFO] Extracting frames from video...")

while True:
    success, frame = cap.read()
    if not success:
        break
    if frame_index % frame_skip_interval == 0:
        extracted_frames.append((frame_index, frame))
    frame_index += 1

cap.release()

# === Train-test split ===
total_frames = len(extracted_frames)
train_count = int(total_frames * train_ratio)

train_frames = []
test_frames = []

for i, (index, frame) in enumerate(extracted_frames):
    if i % test_frame_gap == 0 and len(test_frames) < total_frames - train_count:
        test_frames.append((index, frame))
    else:
        train_frames.append((index, frame))

# === Save frames ===
def save_frames(frames, target_dir, prefix):
    for i, (index, frame) in enumerate(frames, start=1):
        filename = f"{prefix}_{i:05d}.jpg"
        path = os.path.join(target_dir, filename)
        cv2.imwrite(path, frame)

print(f"[INFO] Saving {len(train_frames)} training frames...")
save_frames(train_frames, image_train_dir, prefix=f"{project_name}_train")

print(f"[INFO] Saving {len(test_frames)} testing frames...")
save_frames(test_frames, image_test_dir, prefix=f"{project_name}_test")

print("[✅ DONE] Dataset is ready for annotation and training.")
