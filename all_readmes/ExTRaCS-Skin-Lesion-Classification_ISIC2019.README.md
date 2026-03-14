name:	nusRying/ExTRaCS-Skin-Lesion-Classification_ISIC2019
description:	
--
# ≡ƒö¼ Melanoma Detection using ExSTraCS

PhD Research Project - Week 15 January

## ≡ƒôü Project Structure

This project is organized into numbered directories following the data science workflow:

```
Code/
Γö£ΓöÇΓöÇ 1_Data/                          # ≡ƒôè Dataset files
Γöé   Γö£ΓöÇΓöÇ HAM10000/                    # HAM10000 dataset CSV files
Γöé   ΓööΓöÇΓöÇ ISIC2019/                    # ISIC2019 dataset CSV files
Γöé
Γö£ΓöÇΓöÇ 2_Preprocessing/                 # ≡ƒöº Data preparation
Γöé   Γö£ΓöÇΓöÇ Feature extraction scripts
Γöé   Γö£ΓöÇΓöÇ Data cleaning utilities
Γöé   Γö£ΓöÇΓöÇ hair-removal/                # Hair removal preprocessing
Γöé   Γö£ΓöÇΓöÇ hair_removing/
Γöé   ΓööΓöÇΓöÇ preprocessed_images/
Γöé
Γö£ΓöÇΓöÇ 3_Training/                      # ≡ƒÄ» Model training
Γöé   Γö£ΓöÇΓöÇ Training scripts for various configurations
Γöé   Γö£ΓöÇΓöÇ Cross-validation experiments
Γöé   Γö£ΓöÇΓöÇ Hyperparameter optimization
Γöé   ΓööΓöÇΓöÇ Ensemble methods
Γöé
Γö£ΓöÇΓöÇ 4_Testing/                       # Γ£à Model evaluation
Γöé   Γö£ΓöÇΓöÇ Testing scripts
Γöé   ΓööΓöÇΓöÇ Test result comparisons
Γöé
Γö£ΓöÇΓöÇ 5_Analysis/                      # ≡ƒôê Results analysis
Γöé   Γö£ΓöÇΓöÇ Statistical analysis
Γöé   Γö£ΓöÇΓöÇ Model comparison
Γöé   Γö£ΓöÇΓöÇ Visualization tools
Γöé   ΓööΓöÇΓöÇ rule_visualizations/
Γöé
Γö£ΓöÇΓöÇ 6_Results/                       # ≡ƒÆ╛ Experimental outputs
Γöé   Γö£ΓöÇΓöÇ Training results
Γöé   Γö£ΓöÇΓöÇ Test results
Γöé   Γö£ΓöÇΓöÇ Validation results
Γöé   ΓööΓöÇΓöÇ Optimization outputs
Γöé
Γö£ΓöÇΓöÇ 7_Models/                        # ≡ƒñû Trained models
Γöé   Γö£ΓöÇΓöÇ lcs/                         # LCS models
Γöé   Γö£ΓöÇΓöÇ lcs_aug/                     # Augmented LCS models
Γöé   ΓööΓöÇΓöÇ ensemble_models/             # Ensemble models
Γöé
Γö£ΓöÇΓöÇ 8_Documentation/                 # ≡ƒôÜ Project guides
Γöé   Γö£ΓöÇΓöÇ Experiment guides
Γöé   Γö£ΓöÇΓöÇ Testing documentation
Γöé   Γö£ΓöÇΓöÇ Results analysis reports
Γöé   ΓööΓöÇΓöÇ Quick reference guides
Γöé
Γö£ΓöÇΓöÇ 9_Notebooks/                     # ≡ƒôô Jupyter notebooks
Γöé   Γö£ΓöÇΓöÇ main.ipynb
Γöé   ΓööΓöÇΓöÇ skin-disease-classification.ipynb
Γöé
Γö£ΓöÇΓöÇ 10_Utilities/                    # ≡ƒ¢á∩╕Å Helper scripts
Γöé   ΓööΓöÇΓöÇ Utility scripts and batch files
Γöé
Γö£ΓöÇΓöÇ Best_Model_Deliverable/          # ≡ƒÅå Top performing models
Γöé   Γö£ΓöÇΓöÇ Training & testing scripts for best models
Γöé   Γö£ΓöÇΓöÇ Pre-trained champion models (.pkl)
Γöé   ΓööΓöÇΓöÇ Detailed model documentation
Γöé
Γö£ΓöÇΓöÇ scikit-ExSTraCS-master/          # ≡ƒôª ExSTraCS library
Γöé
ΓööΓöÇΓöÇ README.md                         # This file
```

---

## ≡ƒÄ» Project Overview

This research implements **ExSTraCS** (Extended Supervised Tracking and Classifying System) for melanoma detection using skin lesion images from HAM10000 and ISIC2019 datasets.

### Key Features:
- **ABCD Feature Extraction**: Asymmetry, Border, Color, Diameter features
- **Wavelet Transform**: RGB wavelet features for texture analysis
- **Hybrid Features**: Combination of traditional and deep features
- **LBP & GLCM**: Local Binary Patterns and Gray-Level Co-occurrence Matrix
- **Oversampling**: Handles class imbalance for melanoma detection

---

## ≡ƒÜÇ Quick Start

### 1∩╕ÅΓâú Data Preparation
```bash
cd 2_Preprocessing
python extract_abcd_features.py
python extract_wavelet_features.py
```

### 2∩╕ÅΓâú Model Training
```bash
cd 3_Training
python train_optimized_final.py
```

### 3∩╕ÅΓâú Model Testing
```bash
cd 4_Testing
python test_isic2019.py
```

### 4∩╕ÅΓâú Analysis
```bash
cd 5_Analysis
python analyze_results.py
python statistical_significance.py
```

---

## ≡ƒÅå Best Models

The **Best_Model_Deliverable** folder contains the top-performing models:

| Model | Sensitivity | Specificity | BA | FN |
|:------|:------------|:------------|:---|:---|
| **Balanced Champion (Seed 456)** | 73.4% | 79.1% | 76.2% | 353 |
| **High Sensitivity (Seed 123)** | 74.4% | 78.8% | 76.6% | 340 |
| **Baseline RGB** | 67.4% | 82.3% | 74.9% | 432 |

See [`Best_Model_Deliverable/README_TRAINING_TESTING.md`](Best_Model_Deliverable/README_TRAINING_TESTING.md) for details.

---

## ≡ƒôè Datasets

### HAM10000 (1_Data/HAM10000/)
- Dermatoscopic images of common pigmented skin lesions
- Binary classification: Nevus vs Melanoma
- Training, validation, and test splits
- Augmented training data available

### ISIC2019 (1_Data/ISIC2019/)
- International Skin Imaging Collaboration dataset
- Larger scale melanoma detection challenge
- Binary classification: Nevus vs Melanoma
- Augmented training data available

---

## ≡ƒö¼ Methodology

### Feature Extraction (2_Preprocessing/)
1. **ABCD Features**: Clinical dermatology features
   - Asymmetry score
   - Border irregularity
   - Color variation
   - Diameter measurements

2. **Wavelet Features**: Texture analysis
   - RGB channel wavelet decomposition
   - Multi-scale feature extraction

3. **Traditional Features**: LBP, GLCM
   - Local Binary Patterns for texture
   - Gray-Level Co-occurrence Matrix statistics

### Model Training (3_Training/)
- **ExSTraCS**: Rule-based evolutionary learning
- **Hyperparameter Optimization**: Grid search, population size, iterations
- **Oversampling**: Minority class balancing (1.2x ratio)
- **Cross-Validation**: Multi-seed validation
- **Ensemble Methods**: Multiple model aggregation

### Evaluation (4_Testing/ & 5_Analysis/)
- Sensitivity, Specificity, Balanced Accuracy
- Confusion matrices
- ROC curves and AUC scores
- Statistical significance testing
- False Negative analysis (critical for melanoma detection)

---

## ≡ƒôê Key Results

### Best Performance
- **Highest Sensitivity**: 74.4% (340 missed melanomas out of 1327)
- **Best Balance**: 76.2% BA with 73.4% sensitivity
- **ABCD Impact**: +6-7% sensitivity improvement over RGB baseline

### Research Contributions
Γ£à Novel ABCD feature integration with ExSTraCS
Γ£à Optimized oversampling strategy for melanoma detection
Γ£à Comprehensive hyperparameter analysis
Γ£à Multi-seed validation for robustness

---

## ≡ƒôÜ Documentation

All documentation is located in **8_Documentation/**:

- `EXPERIMENTS_GUIDE.md` - Experiment configurations
- `OPTIMIZED_EXPERIMENTS_GUIDE.md` - Optimization strategies
- `TESTING_README.md` - Testing procedures
- `RESULTS_ANALYSIS.md` - Results interpretation
- `COMPARISON_GUIDE.md` - Model comparison methods
- `ENSEMBLE_GUIDE.md` - Ensemble methodology

---

## ≡ƒ¢á∩╕Å Requirements

- Python 3.7+
- NumPy, Pandas, scikit-learn
- OpenCV (for image processing)
- PyWavelets (for wavelet features)
- matplotlib, seaborn (for visualization)
- ExSTraCS (included in `scikit-ExSTraCS-master/`)

---

## ≡ƒô¥ Notes

### Directory Numbering
The numbered folders (1-10) represent the typical workflow:
1. Start with **Data**
2. **Preprocess** the data
3. **Train** models
4. **Test** performance
5. **Analyze** results
6. Review **Results** outputs
7. Load pre-trained **Models**
8. Read **Documentation**
9. Explore **Notebooks**
10. Use **Utilities** as needed

### Best Practices
- Keep `Best_Model_Deliverable/` for final models only
- Use `6_Results/` for all experimental outputs
- Document experiments in `8_Documentation/`
- Version control with `.git/`

---

## ≡ƒöù Related Work

This project builds upon:
- ExSTraCS: Extended Supervised Tracking and Classifying System
- ISIC Challenge: International Skin Imaging Collaboration
- ABCD Rule: Dermatology clinical assessment criteria

---

## ≡ƒæñ Author

PhD Research - Week 15 January 2026

---

## ≡ƒôî Quick Links

- [Best Models](Best_Model_Deliverable/)
- [Training Scripts](3_Training/)
- [Testing Scripts](4_Testing/)
- [Documentation](8_Documentation/)
- [Analysis Tools](5_Analysis/)

---

**Last Updated**: January 25, 2026

