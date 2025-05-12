# GestureMouse
# 🖱️ Hand-Controlled Mouse & 🎯 Catch the Circle Game

## Overview

This project includes two interactive Python applications that use computer vision and hand gesture recognition:

1. **`WirelessMouse.py`** – Control your computer's mouse using your hand via webcam and MediaPipe.
2. **`CircleGame.py`** – A full-screen game where you try to catch a randomly appearing red circle using your real mouse.

---
## ⚠️ Important Notes

- **MediaPipe is not compatible with Python 3.11 or newer.**  
  Please make sure you are using **Python 3.10 or lower** to run `WirelessMouse.py` successfully.

- To avoid version conflicts, it's recommended to use a **virtual environment** such as:

  - [`venv`](https://docs.python.org/3/library/venv.html):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
  - Or [`conda`](https://docs.conda.io/):
    ```bash
    conda create -n handmouse python=3.10
    conda activate handmouse
    ```

---
## 🔧 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- PyAutoGUI
- MediaPipe (for hand detection)


Install dependencies using:

```bash
pip install opencv-python mediapipe numpy pyautogui
```

## 📁 Files

- `WirelessMouse.py`: Uses webcam + MediaPipe to control mouse movement and simulate left/right clicks with hand gestures.
- `CircleGame.py`: A simple but fun game that increases your score when your mouse cursor touches the circle.

---

## ▶️ How to Run
### 1. Wireless Mouse Control

```bash
python WirelessMouse.py
```
- Move your index finger to control the mouse.

- Touch thumb + index to left-click.

- Touch index + middle to right-click.


### 2. Catch the Circle Game

```bash
python CircleGame.py
```
- Move your mouse to "touch" the red circle.

- Score increases every time you catch it.

- Press q to quit the game.

## 🧠 How it Works

### 1.Wireless Mouse

- Uses MediaPipe Hands to track hand landmarks in real-time.

- Tracks finger positions and calculates distances to determine left/right click.

- Maps index finger position to screen coordinates using interpolation and moves the mouse accordingly.

### 2.Circle Game

- Displays a full-screen black window with a red circle.

- When the mouse cursor overlaps the circle, score increases and a new random circle is generated.





