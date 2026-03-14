name:	nusRying/VisionVault-CV-Suite
description:	
--
# Antigravity CV Project Suite

Unified workspace for five computer vision projects with a single Streamlit launcher (`dashboard.py`).

## Projects

- Hand Gesture Recognition (`Hand_Gesture_Recognition/`)
- HOG + SVM Gesture Recognition (`HOG_SVM_Gesture_Recognition/`)
- Hand Tracking, Air Writing, and Next-Gen Air Writing (`Hand_Tracking_Optical_Flow/`)
- Camera Estimation + Calibration (`Camera_Estimation/`)
- Optic Disc Detection (U-Net) (`Optic_Disc_Detection/`)

## Quick Start

Run from repository root:

```bash
cd "c:/Users/umair/Videos/CV Project 2"
pip install -r requirements-pinned.txt
make run
```

Dashboard pages:

1. Home
2. Hand Gesture Recognition
3. HOG + SVM
4. Hand Tracking & Air Writing
5. Camera Estimation
6. Optic Disc Detection
7. Operations & Artifacts

## Command Reference

Core operations:

```bash
make smoke
make sample-data
make regression-ci
make run
```

Gesture regression:

```bash
python scripts/record_gesture_clips.py --camera_index 0 --clips_per_gesture 5 --seconds 3.5
python scripts/build_gesture_manifest.py --include_negative_nohand
python scripts/gesture_regression.py --manifest sample_data/gestures/manifest.json --report exports/gesture_regression_report.json
python scripts/gesture_regression.py --manifest sample_data/gestures/manifest.json --onnx_gesture_model exports/gesture_head.onnx --report exports/gesture_regression_onnx_report.json
python scripts/gesture_regression.py --manifest sample_data/gestures/manifest_ci.json --report exports/gesture_regression_ci_report.json
```

Next-Gen profile tuning:

```bash
python Hand_Tracking_Optical_Flow/recalibrate_nextgen.py --camera_index 0 --profile desk_cam
python scripts/recalibrate_profiles.py --pairs 0:desk_cam 1:overhead_cam
```

Model export:

```bash
python scripts/export_onnx.py --model optic_disc
```

## Documentation Map

- Dataset quick start: `DOWNLOAD_DATASETS.md`
- Hand Gesture docs: `Hand_Gesture_Recognition/README.md`
- HOG + SVM docs: `HOG_SVM_Gesture_Recognition/README.md`
- Air Writing + Next-Gen docs: `Hand_Tracking_Optical_Flow/README.md`
- Next-Gen full guide: `Hand_Tracking_Optical_Flow/NEXTGEN_AIR_WRITING_GUIDE.md`
- Next-Gen quick reference: `Hand_Tracking_Optical_Flow/NEXTGEN_QUICK_REFERENCE.md`
- Camera Estimation docs: `Camera_Estimation/README.md`
- Optic Disc docs: `Optic_Disc_Detection/README.md`
- Sample data docs: `sample_data/README.md`

## CI and Reproducibility

- Workflow: `.github/workflows/ci.yml`
- CI checks:
  - compile all Python sources
  - generate deterministic sample data
  - run smoke checks
  - run gesture regression against CI manifest (`sample_data/gestures/manifest_ci.json`)

## Notes

- Run scripts from repository root for consistent paths.
- Webcam apps require exclusive camera access.
- If `mediapipe` is unavailable, gesture regression still runs CI no-hand checks but will warn in report output.

