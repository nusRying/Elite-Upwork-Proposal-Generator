name:	nusRying/week-29-january
description:	
--
# Evolutionary Derma-Classifier: Cross-Domain Skin Lesion Analysis

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Research](https://img.shields.io/badge/PhD-Research-orange)

**Repository for PhD Feature Engineering & Evolutionary Learning Experiments**

This project implements a hybrid **Domain-Invariant Feature Learning + Learning Classifier System (ExSTraCS)** framework designed to solve the problem of **domain shift** in dermatological imaging (ISIC 2019 $\rightarrow$ HAM10000).

> **Viral Topics**: `#deep-learning` `#dermatology` `#evolutionary-algorithms` `#explainable-ai` `#medical-imaging` `#python` `#scikit-learn`

---

## ≡ƒô£ How to Cite
If you use this code in your research, please cite:

```bibtex
@article{DerivedFeatures2026,
  title={Enhancing Dermatological Classification through Evolutionary Rule-Based Learning},
  author={PhD Researcher},
  journal={arXiv preprint},
  year={2026}
}
```

---

## ≡ƒÅù∩╕Å Project Architecture

The codebase is organized into modular experiments as defined in the research proposal:

```
Γö£ΓöÇΓöÇ Derived_Features_Champion/       # [CORE] The Final Proposed Model (Zero-Shot)
Γöé   Γö£ΓöÇΓöÇ feature_engine.py            # Extracts ABCD, GLCM, Wavelet Features
Γöé   Γö£ΓöÇΓöÇ pipeline_feature_selection.py# Selects Top 100 Co-adapted Interactions
Γöé   Γö£ΓöÇΓöÇ pipeline_retrain_model.py    # Trains the ExSTraCS LCS Model
Γöé   ΓööΓöÇΓöÇ CHAMPION_TECHNICAL_REPORT.md # Full performance methodology
Γöé
Γö£ΓöÇΓöÇ GA_Mutation_Study/               # [EXP 1] Evolutionary Dynamics Analysis
Γöé   Γö£ΓöÇΓöÇ run_mutation_study.py        # 500k iteration sensitivity sweep
Γöé   ΓööΓöÇΓöÇ snapshots/                   # Model checkpoints (LFS Tracked)
Γöé
Γö£ΓöÇΓöÇ N_Multipliers_Study/             # [EXP 2] Population Sizing Analysis
Γöé   Γö£ΓöÇΓöÇ run_n_study.py               # Testing N=500 to N=6000
Γöé   ΓööΓöÇΓöÇ results/                     # Saturation curves
Γöé
Γö£ΓöÇΓöÇ Transfer_Learning_ISIC_to_HAM/   # [EXP 3] Transfer Learning Baseline
Γöé   ΓööΓöÇΓöÇ run_transfer_learning.py     # Sequential fine-tuning pipeline
Γöé
ΓööΓöÇΓöÇ scikit-ExSTraCS-master/          # [LIB] Custom Extended supervised LCS
```

---

## ΓÜí Quick Start

### 1. Prerequisites
The project relies on specific versions of `numpy` (for LCS rule matching) and `opencv`.

```bash
pip install -r requirements.txt
```

### 2. Running a Prediction (Champion Model)
To use the trained champion model on a new image:

```bash
cd Derived_Features_Champion
python predict_with_champion.py --image "path/to/skin_lesion.jpg"
```

### 3. Reproducing Experiments
To reproduce the transfer learning or mutation studies:

```bash
# Example: Run the transfer learning benchmark
cd Transfer_Learning_ISIC_to_HAM
python run_transfer_learning.py
```

### 4. ≡ƒÉ│ Running with Docker
Avoid dependency hell by using the pre-configured Docker container:

```bash
# Build and start the container in background
docker-compose up -d --build

# Enter the container shell
docker-compose exec classifier bash
```

---

## ≡ƒôè Key Results

| Metric | ISIC 2019 (Training) | HAM 10000 (Zero-Shot) | Stability |
| :--- | :---: | :---: | :---: |
| **Balanced Acc** | **72.28%** | **72.37%** | **+0.09%** |
| **Sensitivity** | 72.39% | 74.05% | High Recall |

**Finding**: The Derived Features approach (72.37%) outperforms standard Computational Transfer Learning (67.6%) on the target domain.

---

## ≡ƒô¥ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

