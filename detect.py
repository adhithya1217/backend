from ultralytics import YOLO

# ✅ Load YOUR trained model
model = YOLO("best.pt")

# Debug (very important)
print("Loaded classes:", model.names)

def detect(frame):
    results = model(frame)

    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detections.append(label)

    return detections