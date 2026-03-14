name:	nusRying/Sentiment140-Sentiment-Analysis
description:	
--
# Sentiment Analysis on Sentiment140 Dataset

## Overview

This project aims to perform sentiment analysis on the **Sentiment140** dataset, which consists of 1.6 million tweets. The goal is to classify tweets into either **Positive** or **Negative** categories using advanced text preprocessing and machine learning ensemble techniques.

## Dataset

The project utilizes the **Sentiment140** dataset, a well-known benchmark for sentiment analysis tasks. Due to the large volume of data (1.6M entries), the project processes a balanced sample of **160,000 tweets** (80,000 positive and 80,000 negative) to maintain computational efficiency while ensuring model robustness.

- **Labels**:
  - `0`: Negative
  - `4` (mapped to `1` in this project): Positive

## Project Workflow

### 1. Data Cleaning & Preprocessing

To convert raw tweets into a format suitable for machine learning, the following steps were performed:

- **Text Normalization**: All text was converted to lowercase.
- **Special Character Removal**: URLs, hashtags, user mentions (@), and non-alphanumeric characters were removed using regular expressions.
- **Stopword Removal**: Common English stopwords (e.g., "the", "is", "at") were filtered out using the NLTK library.
- **Stemming**: Words were reduced to their root form using the **Snowball Stemmer** (e.g., "running" becomes "run").

### 2. Feature Extraction

The cleaned text was vectorized to represent semantic relationships between words, preparing it for the ensemble models.

### 3. Model Training & Evaluation

Two powerful ensemble learning methods were implemented and compared:

- **Gradient Boosting Machine (GBM)**: An iterative ensemble technique that minimizes loss by adding weak learners sequentially.
- **AdaBoost (Adaptive Boosting)**: Focuses on incorrectly classified instances in subsequent iterations to improve performance.

#### Hyperparameter Tuning

Hyperparameters were optimized (likely using **Optuna**) to find the best configuration for `learning_rate` and `n_estimators`.

## Results

The final models achieved the following classification accuracies on the test set:

| Model                       | Accuracy    |
| :-------------------------- | :---------- |
| **Gradient Boosting (GBM)** | **~73.32%** |
| **AdaBoost**                | **~68.64%** |

## Visualizations

The project includes several visualizations to understand the common language used in different sentiments:

- **Word Clouds**: Visual representation of the most frequent terms in positive vs. negative tweets.
- **Data Distribution**: Charts showing the balance of target labels and text length analysis.

## Key Technologies

- **Python**: Core programming language.
- **Libraries**: `Pandas`, `NumPy`, `Scikit-learn`, `NLTK`, `Matplotlib`, `Seaborn`, `WordCloud`.
- **Environment**: Jupyter Notebook / Google Colab.

---

_Created as part of Assignment 3 - i237606_

