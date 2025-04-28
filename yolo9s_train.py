from ultralytics import YOLO

def main():
    model = YOLO('yolov9s.pt')  # 👈 Now using YOLOv9s
    results = model.train(
        data='dataset.yaml',
        epochs=50,
        imgsz=640,
        batch=8,             # More memory available on Colab GPU
        device='cuda',       # GPU
        workers=2,           # Optional
        project='yolo9s_runs',
        name='yolo9s_colab_run'
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
