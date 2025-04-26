from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')
    results = model.train(
        data='dataset.yaml',
        epochs=30,
        imgsz=416,
        batch=2,
        workers=0,
        name='yolo_run'
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
