import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from configurations import HISTORICAL_DATA_BASE_ADDRESS, HISTORY_LENGTH, FORECAST_HORIZON, START_YEAR, END_YEAR, \
    TESTING_SIZE, VALIDATION_SIZE


def main():
    data = pd.read_csv(f"{HISTORICAL_DATA_BASE_ADDRESS}/{START_YEAR}_{END_YEAR}/"
                       f"3_3/without_grouping_plan/"
                       f"{FORECAST_HORIZON}/historical_data h={HISTORY_LENGTH}.csv")
    data.dropna(inplace=True)
    y = np.array(data[['Normal target']]).reshape(-1)
    X = np.array(data.drop(['spatial id', 'temporal id', 'Target (normal)', 'Normal target'], axis=1))
    X_train, y_train = X[:int(len(X) * (1 - TESTING_SIZE))], y[:int(len(y) * (1 - TESTING_SIZE))]
    X_test, y_test = X[int(len(X) * (1 - TESTING_SIZE)):], y[int(len(y) * (1 - TESTING_SIZE)):]
    X_train, X_val, y_train, y_val = \
        train_test_split(X_train, y_train, test_size=VALIDATION_SIZE / (1 - TESTING_SIZE), random_state=1)
    knn_model = KNeighborsClassifier()
    glm_model = LogisticRegression()
    knn_model.fit(X_train, y_train.ravel())
    glm_model.fit(X_train, y_train.ravel())
    knn_validation_predictions = knn_model.predict_proba(X_val)
    glm_validation_predictions = glm_model.predict_proba(X_val)
    knn_validation_predictions_df = pd.DataFrame(data={'real': y_val, 'class 1': knn_validation_predictions[:, 1]})
    glm_validation_predictions_df = pd.DataFrame(data={'real': y_val, 'class 1': glm_validation_predictions[:, 1]})
    knn_validation_predictions_df.to_csv('results/knn/prediction/validation_predictions.csv', index=False)
    glm_validation_predictions_df.to_csv('results/glm/prediction/validation_predictions.csv', index=False)
    knn_testing_predictions = knn_model.predict_proba(X_test)
    glm_testing_predictions = glm_model.predict_proba(X_test)
    knn_testing_predictions_df = pd.DataFrame(data={'real': y_test, 'class 1': knn_testing_predictions[:, 1]})
    glm_testing_predictions_df = pd.DataFrame(data={'real': y_test, 'class 1': glm_testing_predictions[:, 1]})
    knn_testing_predictions_df.to_csv('results/knn/prediction/testing_predictions.csv', index=False)
    glm_testing_predictions_df.to_csv('results/glm/prediction/testing_predictions.csv', index=False)


if __name__ == '__main__':
    main()
