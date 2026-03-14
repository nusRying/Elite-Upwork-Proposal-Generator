name:	nusRying/face-recognition-biometrics
description:	Real-time face recognition with liveness detection, eye blink tracking, and head pose estimation
--
# ≡ƒÄ¡ Face Recognition & Biometrics

A real-time face recognition system with **liveness detection**, **eye blink tracking**, and **head pose estimation** ΓÇö built with Python, OpenCV DNN, `dlib`, and MediaPipe.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green?logo=opencv)
![dlib](https://img.shields.io/badge/dlib-face_recognition-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FaceMesh-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Γ£¿ Features

| Feature                     | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| ≡ƒöì **Face Detection**       | OpenCV DNN (ResNet-10 SSD) ΓÇö fast, accurate, runs on CPU |
| ≡ƒº¼ **Face Recognition**     | 128D face encoding via `face_recognition` (dlib)         |
| ≡ƒæü∩╕Å **Eye Blink Detection**  | Eye Aspect Ratio (EAR) using MediaPipe FaceMesh          |
| ≡ƒöÉ **Liveness Check**       | Blink challenge to verify a live person (anti-spoofing)  |
| ≡ƒº¡ **Head Pose Estimation** | Yaw, Pitch, Roll from 3D face landmarks                  |

---

## ≡ƒôª Installation

> **Windows users**: `dlib` is best installed via conda for a painless experience.

```bash
# Recommended (Windows): create and activate a conda environment
conda create -n face_recog python=3.10 -y
conda activate face_recog
conda install -c conda-forge dlib face_recognition -y
pip install opencv-python mediapipe numpy
```

Alternatively, using pip (requires CMake + C++ build tools on Windows):

```bash
pip install -r requirements.txt
```

---

## ≡ƒÜÇ Quick Start

### Step 1 ΓÇö Enroll your face

```bash
python enroll.py --name "Your Name"
```

- Look at the camera and press **`SPACE`** to capture face samples (5 by default)
- Press **`Q`** to cancel
- Your face encoding is saved to `data/known_faces/`

### Step 2 ΓÇö Run real-time recognition

```bash
python recognize.py
```

**Controls:**

| Key | Action                                          |
| --- | ----------------------------------------------- |
| `L` | Start liveness challenge (blink 3 times in 10s) |
| `R` | Reset blink counter                             |
| `Q` | Quit                                            |

---

## ≡ƒôü Project Structure

```
Face_Recognition_Biometrics/
Γö£ΓöÇΓöÇ src/
Γöé   Γö£ΓöÇΓöÇ face_detector.py    # OpenCV DNN face detection (ResNet-10 SSD)
Γöé   Γö£ΓöÇΓöÇ face_encoder.py     # 128D face encoding & matching
Γöé   ΓööΓöÇΓöÇ biometrics.py       # Blink EAR, liveness check, head pose
Γö£ΓöÇΓöÇ data/
Γöé   ΓööΓöÇΓöÇ known_faces/        # Enrolled face encodings (.pkl) ΓÇö gitignored
Γö£ΓöÇΓöÇ models/                 # Auto-downloaded DNN model weights ΓÇö gitignored
Γö£ΓöÇΓöÇ enroll.py               # Face enrollment CLI script
Γö£ΓöÇΓöÇ recognize.py            # Real-time recognition & biometrics
Γö£ΓöÇΓöÇ requirements.txt
ΓööΓöÇΓöÇ README.md
```

---

## ΓÜÖ∩╕Å Options

### `enroll.py`

```
--name          Name for the enrolled face (required)
--camera        Camera index (default: 0)
--num_samples   Number of samples to capture for averaging (default: 5)
```

### `recognize.py`

```
--camera        Camera index (default: 0)
--tolerance     Match distance threshold ΓÇö lower = stricter (default: 0.5)
--skip_frames   Process every Nth frame for speed (default: 2)
```

---

## ≡ƒ¢á∩╕Å How It Works

1. **Detection** ΓÇö Each frame is passed through a ResNet-10 SSD network to find face bounding boxes.
2. **Encoding** ΓÇö Detected faces are encoded to a 128-dimensional vector using dlib's HOG + deep metric learning.
3. **Matching** ΓÇö The encoding is compared against all enrolled faces using Euclidean distance.
4. **Biometrics** ΓÇö MediaPipe FaceMesh landmarks are used to compute EAR (Eye Aspect Ratio) for blink detection, and PnP pose solving for head pose.
5. **Liveness** ΓÇö The system triggers a blink challenge and verifies 3 distinct blinks before marking a face as "live".

---

## ≡ƒôï Requirements

- Python 3.8+
- OpenCV ΓëÑ 4.5
- dlib (with face_recognition)
- MediaPipe
- NumPy

---

## ≡ƒôä License

MIT License ΓÇö see [LICENSE](LICENSE) for details.

