name:	nusRying/HOG_SVM_Gesture_Recognition
description:	
--
# HOG + SVM Gesture Recognition

Detect hand gestures using Histogram of Oriented Gradients (HOG) features and an SVM classifier.

## Setup
1. Install requirements:
`pip install -r requirements.txt`

## Usage

1. **Collect Data**:
   `python data_collection.py`
   - Place hand in green box.
   - Press `0`, `1`, `2` to save samples for corresponding gestures (Fist, Palm, Peace).
   - Press `3` to save Background samples (empty box).

2. **Train Model**:
   `python train_svm.py`
   - Extracts features and trains SVM.
   - Saves model to `models/svm_model.pkl`.

   (Optional) Train CNN baseline:
   `python train_cnn.py`

3. **Run Inference**:
   `python main_svm.py`
   - Real-time gesture recognition.

