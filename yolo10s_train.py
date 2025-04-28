from ultralytics import YOLO

def main():
    model = YOLO('yolov10s.pt')  # 👈 YOLOv10s for good speed+accuracy
    results = model.train(
        data='dataset.yaml',
        epochs=50,
        imgsz=640,
        batch=8,          # batch 8 should fit easily on Colab GPU
        device='cuda',    # GPU usage
        workers=2,
        project='yolo10s_runs',
        name='yolo10s_colab_run'
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
