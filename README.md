# 🔊 Hand Gesture Volume Control

Control your **system volume** using just your **hand gestures and webcam**!  
This project uses **MediaPipe**, **OpenCV**, and **Pycaw** to detect your fingers and adjust volume based on their distance.

https://user-images.githubusercontent.com/your-demo.gif <!-- Optional: Add demo GIF -->

---

## 🎯 Features

- ✋ Real-time hand tracking using MediaPipe
- 🤏 Detects distance between thumb and index finger
- 🔊 Maps distance to system volume range
- 📈 On-screen volume bar for visual feedback
- 🎥 Webcam-based gesture interface
- 💻 Works on Windows using Pycaw for audio control

---

## 🧰 Tech Stack

- **Python**
- **OpenCV** – Video capture and image drawing
- **MediaPipe** – Hand landmark detection
- **NumPy** – For interpolating volume range
- **Pycaw** – System volume control (Windows only)

---

## 📂 File Structure

```bash
📄 volumecontrol.py  # Main Python script
```
---

## 🚀 How to Run
Clone the repository or copy the code into a .py file.

Install the dependencies:

```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```
Run the script:

```bash
python gesture_volume_control.py
```
Make sure your webcam is connected and functioning properly.

---

## ✋ Hand Gestures

| Gesture | Action             |
|--------|--------------------|
| 🤏     | Decrease volume     |
| 👐     | Increase volume     |

---

## 📸 Screenshots <br>
<!-- Add screenshots if needed -->
Volume bar on screen <br>

Real-time hand detection <br>

Line and circles connecting thumb and index  <br>

---

## 🤝 Credits <br>
MediaPipe <br>

OpenCV  <br>

Pycaw <br>

Idea inspired by Computer Vision gesture control systems <br>
