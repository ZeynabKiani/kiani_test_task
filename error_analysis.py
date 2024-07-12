# -*- coding: utf-8 -*-
"""error_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13z1dJojjyPL1BoqQBYgB0Q6qKUzbBLup
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.ensemble import BalancedBaggingClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_true, y_pred):
    labels = sorted(y_true.unique())
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    fig, ax = plt.subplots(figsize=(8, 6))
    disp.plot(ax=ax, cmap=plt.cm.Blues, values_format='d')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()

def error_analysis(y_true, y_pred, X_test):
    errors = X_test.copy()
    errors['True_Label'] = y_true
    errors['Predicted_Label'] = y_pred
    errors['Correct'] = errors['True_Label'] == errors['Predicted_Label']
    misclassified = errors[errors['Correct'] == False]
    return misclassified

if __name__ == "__main__":

    train_df = pd.read_csv('task_train.csv')
    test_df = pd.read_csv('task_test.csv')

    cols_to_drop = ['Label', 'Unnamed: 0.1', 'Unnamed: 0', 'ID', 'UserID', 'Origin', 'Destination', 'Comment']
    X_train = train_df.drop(cols_to_drop, axis=1)
    X_test = test_df.drop(cols_to_drop, axis=1)
    y_train = train_df['Label']
    y_test = test_df['Label']


    X_train['Created_at'] = pd.to_datetime(X_train['Created_at'])
    X_test['Created_at'] = pd.to_datetime(X_test['Created_at'])

    X_train['Month'] = X_train['Created_at'].dt.month
    X_train['Day'] = X_train['Created_at'].dt.day
    X_train['Hour'] = X_train['Created_at'].dt.hour

    X_test['Month'] = X_test['Created_at'].dt.month
    X_test['Day'] = X_test['Created_at'].dt.day
    X_test['Hour'] = X_test['Created_at'].dt.hour

    X_train = X_train.drop('Created_at', axis=1)
    X_test = X_test.drop('Created_at', axis=1)

    numeric_features = ['Time', 'Income']
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features)
        ])


    base_classifier = RandomForestClassifier(random_state=42)


    oversampler = RandomOverSampler(random_state=42)


    balanced_bagging_classifier = BalancedBaggingClassifier(
        base_estimator=base_classifier,
        sampling_strategy='auto',
        replacement=False,
        random_state=42
    )


    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', balanced_bagging_classifier)
    ])


    X_resampled, y_resampled = oversampler.fit_resample(X_train, y_train)

    pipeline.fit(X_resampled, y_resampled)

    # predict on the test set###############
    y_pred = pipeline.predict(X_test)

    # save predictions to a CSV file
    pd.DataFrame({'Predictions': y_pred}).to_csv('test_predicted.csv', index=False)

    # Evaluate the model##############
    print("Evaluation on Test Data:")
    print(classification_report(y_test, y_pred))

    #  error analysis part ###########################
    plot_confusion_matrix(y_test, y_pred)
    misclassified = error_analysis(y_test, y_pred, X_test)
    print("\nMisclassified Examples:")
    print(misclassified.head())