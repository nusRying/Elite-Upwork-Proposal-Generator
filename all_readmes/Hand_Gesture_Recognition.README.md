name:	nusRying/Hand_Gesture_Recognition
description:	
--
# Hand Gesture Recognition

This project implements a real-time hand gesture recognition system using MediaPipe and a Random Forest Classifier.

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Collect Data:
   Run the data collection script to record your own gestures.
   ```bash
   python data_collection.py
   ```
   - Press keys `0-9` to save samples for that class ID.
   - Example mapping:
     - 0: Fist
     - 1: Open Palm
     - 2: Thumbs Up
     - ... (Defined in `main.py`)
   - Collect at least 50-100 samples per gesture for good results.
   - Press `q` to quit.

3. Train Model:
   Train the classifier on the collected data.
   ```bash
   python train_classifier.py
   ```
   This will save `models/gesture_classifier.pkl`.

## Usage

Run the real-time application:

```bash
python main.py
```
This will open your webcam and start predicting gestures.

