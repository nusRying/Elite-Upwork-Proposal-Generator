name:	nusRying/Predictive-Modeling-COVID19-Classification
description:	
--
# Predictive Modeling for COVID-19 Patient Classification

## Project Overview

This project focuses on the development of predictive models to classify COVID-19 patients based on their risk levels and clinical outcomes. By leveraging a large-scale dataset, the project aims to assist health authorities in efficient resource allocation and patient management.

## Dataset

The dataset was provided by the **Mexican government** and consists of anonymized patient-related information:

- **Total Entries**: 1,048,575 unique patients.
- **Initial Features**: 21 unique features (including age, sex, comorbidities, and medical unit type).
- **Target Variable**: `CLASIFFICATION_FINAL` (Values 1-3 indicate COVID-19 diagnosis degrees; 4+ indicate non-carrier or inconclusive results).

## Methodology

The project employs a modern and highly automated machine learning pipeline:

### 1. Data Preprocessing

- Conversion of `DATE_DIED` into a binary survival feature.
- Handling of missing data encoded as `97` (Does not apply) and `99` (Unknown).
- Categorical variable encoding and normalization.

### 2. Automated Feature Engineering

- Extensive use of the **Featuretools** library.
- Implementation of **Deep Feature Synthesis (DFS)** with `add_numeric` and `multiply_numeric` primitives.
- Feature set expansion from 21 initial features to over **440 engineered features**.

### 3. Multi-Stage Feature Selection

- **Correlation Analysis**: Removed features with a correlation > 0.85.
- **Variance Thresholding**: Removed features with variance < 0.1.
- **Recursive Feature Elimination (RFE)**: Used ensemble model importance to select the most impactful features for final training.

### 4. Machine Learning Models

Multiple ensemble and advanced algorithms were evaluated:

- **Gradient Boosting Machine (GBM)**
- **XGBoost Classifier**
- **Random Forest**
- **Extra Trees**
- **AdaBoost**
- **Voting Classifier** (Ensemble of top performers)

### 5. Hyperparameter Optimization

- Utilized **Optuna** for state-of-the-art Bayesian optimization of model hyperparameters.
- Used **GridSearchCV** and Scikit-learn Pipelines for systematic tuning.

## Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn)
- **Featuretools** (Automated Feature Engineering)
- **Optuna** (Hyperparameter Tuning)
- **XGBoost** (Advanced Modeling)
- **Matplotlib & Seaborn** (Data Visualization)

## Results

The project demonstrates the effectiveness of automated feature engineering in capturing complex patient interactions. Initial models achieved a testing accuracy of approximately **54%** across multiple classification categories, providing a robust baseline for clinical decision support.

---

**Author**: M. Awais Tariq (MS-AI)
**Project Category**: Applied Machine Learning (AML)

