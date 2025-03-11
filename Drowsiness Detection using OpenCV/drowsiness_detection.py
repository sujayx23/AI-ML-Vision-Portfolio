import sys
from scipy.spatial import distance as dist
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import face_recognition
import cv2
import threading
import subprocess
import os

# Global flag to prevent multiple alerts
alarm_playing = False

# Function to play the alarm sound and text warning for 5 seconds
def play_alarm():
    global alarm_playing
    alert_path = "/Users/nithishsujay/Documents/AI-ML-showcase/Drowsiness Detection using OpenCV/Alert1.mp3"

    if os.path.exists(alert_path) and not alarm_playing:
        alarm_playing = True
        print(f"[INFO] Playing alarm sound for 5 seconds: {alert_path}")

        # Start audio and speech in separate subprocesses
        sound_process = subprocess.Popen(['afplay', alert_path])
        speech_process = subprocess.Popen(['say', 'Warning! You are feeling drowsy!'])

        # Let the alarm play for 5 seconds, then terminate
        time.sleep(5)
        sound_process.terminate()
        speech_process.terminate()

        alarm_playing = False
    else:
        if not os.path.exists(alert_path):
            print(f"[ERROR] Alarm file not found at: {alert_path}")

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Initialization
count = 0
ear_threshold = 0.25
frame_check = 20

# Start the video stream
print("[INFO] starting video stream thread...")
vs = VideoStream(src=0).start()
time.sleep(1.0)

# Loop over frames from the video stream
while True:
    frame = vs.read()
    if frame is None:
        print("[ERROR] Failed to grab frame.")
        break
    
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect face landmarks
    face_mark = face_recognition.face_landmarks(frame)

    # Initialize EAR as None for this frame
    ear = None

    for i in face_mark:
        left_eye = i["left_eye"]
        right_eye = i["right_eye"]

        # Draw eye contours
        left_eye_points = np.array(left_eye)
        right_eye_points = np.array(right_eye)
        cv2.polylines(frame, [left_eye_points], True, (0, 255, 0), 1)
        cv2.polylines(frame, [right_eye_points], True, (0, 255, 0), 1)

        # Calculate EAR
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        ear = (left_ear + right_ear) / 2

        # Debugging: Print EAR to verify calculations
        print(f"[INFO] Calculated EAR: {ear:.2f}")

    # Check EAR and trigger alarm if necessary
    if ear is not None:
        if ear < ear_threshold:
            count += 1
            print("[INFO] EAR below threshold, count:", count)  # Debug count increment
            if count >= frame_check:
                threading.Thread(target=play_alarm).start()
                # Show ALERT text in red
                cv2.putText(frame, "ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            count = 0

        # Display EAR in red if it's below the threshold
        if ear < ear_threshold:
            cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            # Display EAR in green if it's normal
            cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        # Show message if no face is detected
        cv2.putText(frame, "No Face Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cv2.destroyAllWindows()
vs.stop()
sys.exit()
