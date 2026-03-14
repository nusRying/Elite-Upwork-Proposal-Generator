name:	nusRying/Traffic-Signs-Recognition
description:	Traffic Signs Recognition system with 43-class classification and live webcam support
--
# ≡ƒÜª Traffic Sign Intelligence

# ≡ƒÜª SignIntel: Real-Time Traffic Sign Intelligence

A professional-grade Computer Vision system for real-time traffic sign recognition using a custom-reconstructed MobileNetV2 architecture.

![Dashboard Interface](https://cdn-icons-png.flaticon.com/512/3426/3426033.png)

## ≡ƒ¢░∩╕Å Intelligence Control Center (v2.0)

The project features a high-fidelity Streamlit dashboard with a dual-mode detection engine:

- **≡ƒô╖ LIVE RADAR**: Real-time traffic sign capture and analysis via laptop camera sensors.
- **≡ƒôé FILE INTAKE**: High-resolution telemetry analysis for uploaded image files.
- **≡ƒôè NEURAL LOGITS**: Interactive Top-5 probability distribution visualization via Plotly.
- **≡ƒºá DETECT HISTORY**: Session-based history tracking for recent classifications.

## ≡ƒ¢á∩╕Å Neural Architecture

The system uses a custom-reconstructed MobileNetV2 backbone to bypass framework versioning conflicts (Keras 2/3 compatibility).

- **Base Model**: MobileNetV2 (Pre-trained on ImageNet, fine-tuned).
- **Custom Top**: GlobalAveragePooling2D ΓåÆ Dropout (0.2) ΓåÆ Dense (256, ReLU) ΓåÆ Dense (43, Softmax).
- **Weights Logic**: Precision-mapped loading from low-level NumPy arrays (`.npz`).
- **Preprocessing**: Optimized TensorFlow operations for sub-second inference latency.

## ≡ƒôü Project Structure & Data

To provide a complete out-of-the-box experience, this repository includes:

- **`data/`**: Extracted GTSRB images (Training/Test sets). Note: Large `.zip` archives are excluded to respect GitHub's file limits.
- **`models/`**: Complete set of trained models and weight files.

## ≡ƒÜÇ Getting Started

### Prerequisites

- Python 3.8+
- Conda (Recommended)

### Installation

```powershell
conda activate revival
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### 4. High-Performance Batch Processing

Process an entire folder and export results:

```bash
python batch_predict.py --input path/to/images --output outputs
```

---

## ≡ƒ¢á∩╕Å Project Structure

- `app.py`: CLI entry point (Webcam/Image modes).
- `gradio_app.py`: High-fidelity web interface.
- `batch_predict.py`: Concurrent batch processing engine.
- `src/`: Core logic (model loading, detection, utils).
- `models/`: Contains both Keras and optimized TFLite models.
- `scripts/`: Optimization and utility scripts.

---

## ≡ƒôè Model Optimization

We optimized the original 28MB Keras model using **Float16 Quantization**, resulting in a **4.9MB TFLite** model (~82% reduction) without significant accuracy loss, making it ideal for edge deployment.

---

## ≡ƒô¥ License

This project is open-source and available under the MIT License.

