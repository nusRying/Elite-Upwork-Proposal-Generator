name:	nusRying/Multiclass-Classification
description:	
--
# Multiclass Classification

## Purpose
This project explores multiclass skin-lesion classification using engineered feature sets (LBP, GLCM, wavelet, and color) and feature-fusion experiments across HAM10000 and ISIC2019 datasets.

## Data files
- `ham10000_*` CSVs: feature tables for the HAM10000 dataset (raw, normalized, and fused variants)
- `isic2019_*` CSVs: feature tables for the ISIC2019 dataset (raw, normalized, and fused variants)
- `lcs/`: EXSTRaCS fold results and summary JSON/CSV outputs
- `color_no_foldnorm/`: color feature experiments without fold normalization

## Key scripts and notebooks
- `main.ipynb`: primary notebook workflow
- `feature fusion.ipynb`: fusion experiments
- `fusion_Training.py`: fusion model training script
- `per_fold_normalization_training.py`: training with per-fold normalization
- `color_Fusion_Training_with_fold_notmalization.py`: color fusion with fold normalization
- `color_Fusion_Training_without_fold_notmalization.py`: color fusion without fold normalization
- `extract_color_features.py`: extract color features
- `normalize_color_features.py`: normalize color feature tables
- `count_classes.py`: class-count utility

## How to run
1) Ensure the required CSVs are present in the project root.
2) Run a notebook:
   - Open `main.ipynb` or `feature fusion.ipynb` and execute cells in order.
3) Or run a script from the project root:
   - `python fusion_Training.py`
   - `python per_fold_normalization_training.py`
   - `python color_Fusion_Training_with_fold_notmalization.py`

Notes: adjust paths or dataset locations inside the scripts/notebooks as needed for your local setup.
