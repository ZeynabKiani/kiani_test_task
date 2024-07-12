# Project Report

## Overview

This project focuses on training a machine learning model to handle class imbalance in a dataset. The main challenge encountered was the significant class imbalance, where one class was underrepresented compared to the other. To address this, several imbalance methods were evaluated, with the chosen approach being Training Balanced Bagging with Random Oversampling due to its performance in achieving a balanced F1 score.

## Project Parts

### 1. Data Preprocessing

- Extracted temporal features ('Month', 'Day', 'Hour') from 'Created_at'.
- Applied scaling to numeric features ('Time' and 'Income').

### 2. Model Training

- Utilized RandomForest as the base estimator within Balanced Bagging Classifier.
- Implemented various resampling techniques:
  - Random Oversampling
  - SMOTE
  - ADASYN
  - Random Undersampling

### 3. Imbalance Methods

- Chose Training Balanced Bagging with Random Oversampling due to its effectiveness in handling class imbalance and maximizing the F1 score.

### 4. Performance Evaluation

- Evaluated model performance using classification metrics such as F1 score, precision, and recall.
- Random Oversampling method demonstrated the most balanced performance across classes, with the F1 score being the primary evaluation metric.

## Conclusion

The project successfully addressed the challenge of class imbalance through the implementation of various resampling techniques. Training Balanced Bagging with Random Oversampling emerged as the preferred method due to its balanced performance metrics, particularly in improving the F1 score for both classes.

## Future Work

- Explore additional feature engineering techniques to further enhance model performance.
- Investigate ensemble methods or advanced algorithms to handle class imbalance more effectively.

