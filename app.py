import streamlit as st
import cv2
import time
from detect import detect
from gesture_map import gesture_map
from speech import speak

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Sign Language App", layout="wide")

st.title("🧏 Sign Language Learning App")
st.markdown("### Real-time Gesture → Alphabet → Meaning → Speech")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Controls")

run = st.sidebar.toggle("Start Camera")
clear_history = st.sidebar.button("🗑 Clear History")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

if clear_history:
    st.session_state.history = []

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

alphabet_box = col1.empty()
meaning_box = col2.empty()

status_box = st.empty()
fps_box = st.empty()

frame_window = st.image([])

cap = cv2.VideoCapture(0)

last_text = ""
prev_time = 0

# ---------------- MAIN LOOP ----------------
while run:
    ret, frame = cap.read()
    if not ret:
        st.error("❌ Camera not working")
        break

    labels = detect(frame)

    detected_flag = False

    for label in labels:
        detected_flag = True
        alphabet = label
        meaning = gesture_map.get(label, "Unknown")

        # Draw on frame
        cv2.putText(frame, f"{alphabet} - {meaning}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 0), 2)

        # Update UI boxes
        alphabet_box.markdown(f"## 🔤 Alphabet: `{alphabet}`")
        meaning_box.markdown(f"## 💬 Meaning: `{meaning}`")

        # Add to history
        if meaning != last_text:
            st.session_state.history.append(meaning)

            try:
                speak(meaning)
            except:
                pass

            last_text = meaning

    # ---------------- STATUS ----------------
    if detected_flag:
        status_box.success("✅ Gesture Detected")
    else:
        status_box.warning("⚠ No Gesture Detected")

    # ---------------- FPS ----------------
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    fps_box.markdown(f"### ⚡ FPS: `{int(fps)}`")

    # Convert BGR → RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_window.image(frame)

cap.release()

# ---------------- HISTORY PANEL ----------------
st.sidebar.markdown("## 🧾 Detection History")

if st.session_state.history:
    for item in st.session_state.history[-10:][::-1]:
        st.sidebar.write(f"👉 {item}")
else:
    st.sidebar.write("No detections yet")