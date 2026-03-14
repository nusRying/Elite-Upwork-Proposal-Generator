name:	nusRying/deep-features-hybrid-v2-safety-standalone
description:	Standalone reproducible bundle for Hybrid Optimized v2 (Safety) skin lesion classification experiment
--
# Standalone Bundle: Hybrid Optimized v2 (Safety)

This folder is a self-contained reproduction package for the best external-balanced model setting:

- Model family: `pipeline_hybrid_optimized.py`
- Preferred operating point: **`safety` threshold**
- Best external balanced accuracy observed: **0.7506**

## Included Contents

- `pipeline_hybrid_optimized.py` ΓÇö training + evaluation pipeline (internal + external)
- `project_paths.py` ΓÇö local path resolver for this bundle
- `data/features/` ΓÇö required hybrid feature CSVs
- `data/metadata/` ΓÇö required metadata CSVs
- `external/scikit-ExSTraCS-master/` ΓÇö ExSTraCS dependency
- `models/hybrid_model_v2.pkl` ΓÇö trained model artifact
- `results/results_hybrid_v2.json` ΓÇö saved metrics (std + safety)
- `results/DETAILED_RESULTS_REPORT.md` ΓÇö full experiment report

## Reproduce from this folder

Run from inside this folder (`standalone_hybrid_v2_safety`):

```powershell
python -m pip install -r requirements.txt
python pipeline_hybrid_optimized.py
```

This will regenerate:
- `results/results_hybrid_v2.json`
- `models/hybrid_model_v2.pkl`

## Quick run helper

```powershell
powershell -ExecutionPolicy Bypass -File .\run_reproduce.ps1
```

## Notes

- Training is compute-intensive (`500000` learning iterations).
- The pipeline evaluates two thresholds: `std` and `safety`; for clinical recall emphasis, use `safety` metrics from `results/results_hybrid_v2.json`.
- If your environment is missing optional GPU support, CPU execution will still run but slower.

