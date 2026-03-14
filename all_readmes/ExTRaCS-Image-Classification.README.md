name:	nusRying/ExTRaCS-Image-Classification
description:	
--
# LCS ExSTraCS Experiments

Scripts and utilities for feature extraction and ExSTraCS experiments on skin lesion datasets
(HAM10000, ISIC2019). The workflow is:
1) build feature CSVs from images, 2) run ExSTraCS baselines or cross-validation, 3) save
fold and summary metrics to disk.

## Project layout
- `data/clean/`: local image folders and binary label CSVs (not generated here).
- `data/raw/`: original datasets (not generated here).
- `features/`: reusable feature extraction helpers (wavelets, semantics).
- `results/csv/`: generated feature CSVs (LBP, GLCM, Wavelet) and scripts.
- `results/lcs/`: experiment runners and experiment outputs.
- `notebooks/`: exploratory notebooks.
- `scripts/`: small helper scripts.
- `external/scikit-ExSTraCS-master/`: local copy of the ExSTraCS implementation.

## Requirements
- Python 3.x
- Packages: `numpy`, `pandas`, `scikit-learn`, `scikit-image`, `opencv-python`,
  `pywavelets`, `tqdm`
- ExSTraCS module available as `skExSTraCS` (local repo or installed package).

## Feature extraction
LBP and GLCM (edit `DATASET_NAME` in the script):
```bash
python results/csv/feature_extractor.py
```

Wavelet features:
```bash
python results/csv/create_wavelet_csv.py
```

Optional normalization for wavelet CSVs (edit paths if needed):
```bash
python results/csv/create_wavelets_normalized.py
```

## Run experiments
Baseline fit (sanity check):
```bash
python results/lcs/run_exstracs_baseline.py
```

Cross-validation with parameter grid:
```bash
python results/lcs/run_exstracs_experiments.py
```

Cross-validation per dataset and feature set:
```bash
python results/lcs/run_exstracs_experiments_cv.py
```

## Outputs
- Feature CSVs saved under `results/csv/` (e.g., `ham10000_glcm.csv`).
- CV summaries and fold-level metrics saved under `results/lcs/` with timestamped names.

## Notes
- Input CSVs are expected to include `label` and optionally `image` columns.
- Paths in some scripts are dataset-specific; update them if your folder layout differs.

