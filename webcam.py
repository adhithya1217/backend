import cv2
from detect import detect
from gesture_map import get_text
from speech import speak

def run_webcam():
    cap = cv2.VideoCapture(0)
    last_text = ""   # ✅ track previous output

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        labels = detect(frame)

        for label in labels:
            text = get_text(label)

            cv2.putText(frame, text, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

            # ✅ speak only if new gesture detected
            if text != last_text:
                speak(text)
                last_text = text

        cv2.imshow("Sign Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()