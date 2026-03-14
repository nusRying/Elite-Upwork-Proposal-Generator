name:	nusRying/Sign-Language-Recognition-Using-Image-Processing-and-Machine-Learning
description:	
--
# Sign Language Recognition Using Image Processing and Machine Learning

This repository contains a multi-level sign language recognition system:
- Level 1: Static alphabet recognition (A-Z) with CNN/classical models
- Level 2: Word recognition with LSTM
- Level 3: Sentence-style recognition with Transformer
- Streamlit real-time app in `app.py`

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install PyTorch for your platform (CPU or CUDA build):
- Use the command from the official PyTorch install page for your OS/CUDA version.
- The app and GPU training scripts require `torch` and `torchvision`.

3. Launch the app:
```bash
streamlit run app.py
```
Or on Windows:
```bash
run.bat
```

## App Modes and Expected Model Files

`app.py` expects these checkpoints in `models/`:
- `model_cnn_gpu_torch.pth` for Level 1 (Alphabet)
- `model_lstm_gpu_torch.pth` for Level 2 (Word)
- `model_transformer_gpu_torch.pth` for Level 3 (Transformer)

If a model file is missing, the app shows an error in the sidebar/UI.

## Static Dataset Workflow (Alphabet)

### Option A: Download Kaggle ASL Alphabet
```bash
python src/download_dataset.py
```

### Option B: Build processed landmark dataset (for classical model)
```bash
python src/create_dataset.py
python src/train_classifier.py
```

### Train CNN
- TensorFlow version:
```bash
python src/train_cnn.py
```
- PyTorch GPU version (recommended for native Windows GPU):
```bash
python src/train_cnn_gpu.py
```

### Evaluate CNN (PyTorch)
```bash
python src/evaluate_cnn_gpu.py
```

## Sequence Dataset Workflow (LSTM/Transformer)

Sequence classes default to:
`hello`, `thanks`, `yes`, `no`, `i`, `love`, `you`, `please`

### Collect sequence keypoints from webcam
```bash
python src/collect_sequences.py --no-sequences 30 --sequence-length 30
```

### Or generate synthetic sequences from static letter features
```bash
python src/generate_sequences_from_spelling.py --no-sequences 30 --sequence-length 30
```

### Validate coverage
```bash
python src/check_sequence_coverage.py --min-per-class 20
```

### Train sequence models (PyTorch GPU)
```bash
python src/train_lstm_gpu.py --epochs 120 --batch-size 16 --num-workers 0 --min-sequences-per-class 20 --no-sequences 120
python src/train_transformer_gpu.py --epochs 120 --batch-size 16 --num-workers 0 --min-sequences-per-class 20 --no-sequences 120
```

`--no-sequences` is now enforced in the GPU training loaders.

## ASL Citizen Workflow

Place extracted ASL Citizen data on disk, then:

1. Dry-run metadata and video discovery:
```bash
python src/prepare_asl_citizen_sequences.py --dataset-root "C:\path\to\ASL_Citizen" --dry-run
```

2. Generate sequences:
```bash
python src/prepare_asl_citizen_sequences.py --dataset-root "C:\path\to\ASL_Citizen" --clear-output --sequences-per-action 120 --sequence-length 30
```

3. Verify sequence completeness:
```bash
python src/check_sequence_coverage.py --min-per-class 20
```

4. Train LSTM/Transformer:
```bash
python src/train_lstm_gpu.py --epochs 120 --batch-size 16 --num-workers 0 --min-sequences-per-class 20 --no-sequences 120
python src/train_transformer_gpu.py --epochs 120 --batch-size 16 --num-workers 0 --min-sequences-per-class 20 --no-sequences 120
```

## Inference Scripts

- Classical model:
```bash
python src/inference_classifier.py
```
- CNN PyTorch:
```bash
python src/inference_cnn_gpu.py
```
- LSTM:
```bash
python src/inference_lstm.py
```
- Transformer:
```bash
python src/inference_transformer.py
```

## Notes

- TensorFlow GPU on native Windows can be limited depending on version/CUDA setup.
- PyTorch GPU scripts are the primary path for GPU training/inference in this repo.
- The Streamlit app includes in-session camera stop controls plus keyboard quit (`q`).

## Directory Structure

- `data/`: Raw, processed, and sequence datasets
- `src/`: Training, inference, preprocessing, and utility scripts
- `models/`: Saved checkpoints and model metadata
- `reports/`: Evaluation outputs (classification reports and confusion matrices)

