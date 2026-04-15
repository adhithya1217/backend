from ultralytics import YOLO

model = YOLO("best.pt")

# Run real-time detection
model.predict(source=1, show=True)
