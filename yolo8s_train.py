from ultralytics import YOLO

def main():
    model = YOLO('yolov8s.pt')  # 👈 use yolov8s.pt
    results = model.train(
        data='dataset.yaml',
        epochs=50,          # ⬅️ You can increase this later if you want
        imgsz=640,          # 👈 standard 640x640 image size
        batch=2,            # ⬅️ Batch 2 should be okay on CPU (if slow, reduce to 1)
        device='cuda:0',       
        workers=0,
        project='yolo8s_runs',  # Save results in clean folder
        name='yolo8s_gpu_run'
    )

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
