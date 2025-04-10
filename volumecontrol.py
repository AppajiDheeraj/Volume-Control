import cv2
import mediapipe as mp
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize camera
cap = cv2.VideoCapture(0)

# Access system volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the positions of the index finger and thumb
            index_finger = hand_landmarks.landmark[8]  # Index fingertip
            thumb = hand_landmarks.landmark[4]  # Thumb tip

            h, w, _ = frame.shape
            x1, y1 = int(index_finger.x * w), int(index_finger.y * h)
            x2, y2 = int(thumb.x * w), int(thumb.y * h)

            # Draw circles on the fingers
            cv2.circle(frame, (x1, y1), 10, (0, 255, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

            # Calculate distance between index finger and thumb
            distance = math.hypot(x2 - x1, y2 - y1)

            # Map distance to volume range (0 to 100)
            vol = np.interp(distance, [30, 200], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)

            # Display volume level on screen
            vol_bar = np.interp(distance, [30, 200], [400, 150])
            cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
            cv2.rectangle(frame, (50, int(vol_bar)), (85, 400), (0, 255, 0), -1)

    # Show the frame
    cv2.imshow("Gesture Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()