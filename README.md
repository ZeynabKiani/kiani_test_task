

# Balanced Bagging Classifier with Feature Engineering

## Overview

This project trains a machine learning model using a Balanced Bagging Classifier to handle class imbalance. It includes feature engineering from 'Created_at' and deploys the model using FastAPI for predictions.

## Components

- **Feature Engineering**: Extracts temporal features ('Month', 'Day', 'Hour') from 'Created_at'.
- **Model**: Uses RandomForest as base estimator with various imbalance methods (Random Oversampling, SMOTE, ADASYN, Random Undersampling).
- **Deployment**: FastAPI serves the model via HTTP API (`/predict/`).

## Usage

1. **Installation**: Clone repository, install dependencies (`requirements.txt`).

2. **Training**: Run `train_model.py` to preprocess, train, and save model (`balanced_bagging_model.joblib`).

3. **Deployment**: Start FastAPI server with `uvicorn app:app --reload`.

4. **Prediction**: Send POST requests to `http://localhost:8000/predict/` with JSON data (`Time`, `Income`, `Created_at`).

5. **Response**: Returns JSON with predicted class (`prediction`) and probability (`probability`).

