# from flask import Flask, jsonify
# from flask_cors import CORS
# import cv2
# import base64
# from detect import detect
# from gesture_map import get_text

# app = Flask(__name__)
# CORS(app)

# # ✅ Use working camera index (you said 1 works)
# cap = cv2.VideoCapture(0)

# @app.route("/detect")
# def detect_api():
#     if not cap.isOpened():
#         return jsonify({
#             "alphabet": "",
#             "meaning": "Camera Not Open",
#             "image": ""
#         })

#     ret, frame = cap.read()

#     if not ret:
#         return jsonify({
#             "alphabet": "",
#             "meaning": "Camera Error",
#             "image": ""
#         })

#     # 🧠 YOLO detection
#     labels = detect(frame)

#     if labels:
#         label = labels[0]
#         meaning = get_text(label)
#     else:
#         label = ""
#         meaning = "No Gesture"

#     # 🔥 Convert frame → base64 (for frontend display)
#     _, buffer = cv2.imencode('.jpg', frame)
#     img_base64 = base64.b64encode(buffer).decode('utf-8')

#     return jsonify({
#         "alphabet": label,
#         "meaning": meaning,
#         "image": img_base64
#     })


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 🔥 MODE SWITCH (VERY IMPORTANT)
USE_CAMERA = False   # ✅ False for deployment, True for local

if USE_CAMERA:
    import cv2
    import base64
    from detect import detect
    from gesture_map import get_text

    # ✅ Try different camera index if needed (0 or 1)
    cap = cv2.VideoCapture(0)

@app.route("/")
def home():
    return "Backend Running 🚀"

@app.route("/detect")
def detect_api():

    # 🧠 LOCAL MODE (REAL CAMERA)
    if USE_CAMERA:
        if not cap.isOpened():
            return jsonify({
                "alphabet": "",
                "meaning": "Camera Not Open",
                "image": ""
            })

        ret, frame = cap.read()

        if not ret:
            return jsonify({
                "alphabet": "",
                "meaning": "Camera Error",
                "image": ""
            })

        # YOLO detection
        labels = detect(frame)

        if labels:
            label = labels[0]
            meaning = get_text(label)
        else:
            label = ""
            meaning = "No Gesture"

        # Convert frame → base64
        _, buffer = cv2.imencode('.jpg', frame)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        return jsonify({
            "alphabet": label,
            "meaning": meaning,
            "image": img_base64
        })

    # 🌐 DEPLOY MODE (NO CAMERA)
    else:
        return jsonify({
            "alphabet": "A",
            "meaning": "Demo Mode",
            "image": ""
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)