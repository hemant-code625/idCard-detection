# 🧪 YOLOv8 ID Card Detection

This project uses **YOLOv8 (You Only Look Once)** for real-time object detection of ID cards from images or webcam streams. It is trained on a custom dataset of ID cards annotated using **Label Studio**.

---

## 📂 Project Structure

```
project/
├── idcard_dataset/
│   ├── images
|   |        ├── train
|   |        └── val
│   └── labels
|   |       ├── train
|   |       └── val
├── custom_data.yaml
├── data_extraction.py
├── yolov8n.pt
├── README.md
```

- Run `data_extraction.py` to extract images from your video clip for the training dataset.
- It will generate the dataset directory structre for you.
- After annotation, place the .txt files in the respective labels directories within the train and val (validation) folders.

> Note: YOLOv8 automatically looks for annotation files in a `labels/` directory that mirrors the structure of the `images/` directory.
> So if you have images in `images/train`, it expects corresponding `.txt` annotation files in `labels/train` with the same base filenames.
> This convention allows YOLOv8 to work seamlessly without explicitly specifying the path to labels.

---

## 🧐 Model Info

- **Base model**: YOLOv8n (nano)
- **Framework**: Ultralytics YOLOv8
- **Custom-trained**: Yes, on ID card images
- **Annotations**: Created using **Label Studio**
- **Output**: Bounding box around detected ID cards

---

## 🚀 Installation

Make sure you have Python ≥ 3.8 and installed dependencies.

```bash
conda create -n idcard python=3.10 -y
conda activate idcard

pip install ultralytics opencv-python
```

---

## 🏋️ Training (Optional)

If you want to retrain or continue training:

```bash
yolo task=detect mode=train model="C:\Users\admin\runs\detect\train14\weights\last.pt" data=custom_data.yaml epochs=100 resume=True
```

---

## 🔍 Inference (Detection)

### ▶️ Detect from an image

```bash
yolo task=detect mode=predict model=runs/detect/train14/weights/best.pt source="path_to_image.jpg"
```

### 📹 Real-time detection using webcam

```bash
yolo task=detect mode=predict model=runs/detect/train14/weights/best.pt source=0
```

> Replace `best.pt` with `last.pt` if you prefer using the final checkpoint instead of the best-performing one.

---

## 📊 Results

- Inference results (images with detections) will be saved in a new `runs/detect/predictXX/` folder.

---

## 🚫Troubleshooting

- If training crashes with a memory or `WinError 1455`, try:

  - Setting `workers=0`
  - Disabling AMP with `amp=False`
  - Ensuring enough virtual memory is allocated

- For example: Optimized for lower VRAM GPU pc, make sure that background apps are not running while training.

```bash
    yolo task=detect mode=train data=custom_data.yaml model=yolov8n.pt imgsz=640 batch=1 workers=0 amp=False
```

---

## 👋 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- Custom ID card dataset annotated using **Label Studio**

---

## 🎉 Demo
![u1](https://github.com/user-attachments/assets/15fa5224-15f3-423e-8c70-d0ca9bd92707)
![u2](https://github.com/user-attachments/assets/2cbd688b-e854-4b7c-b47a-48fc8ea99132)
![u3](https://github.com/user-attachments/assets/4f25dc78-e890-4374-ae27-23efaf35c978)
![u4](https://github.com/user-attachments/assets/487efa11-cd3e-47f2-9870-5fda1986f53a)

---
## 🗕️ Author

Hemant – _YOLOv8 ID Card Detection Project_

Feel free to fork and improve the project! 🚀
