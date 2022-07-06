import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ParameterGrid

from configurations import HISTORICAL_DATA_BASE_ADDRESS, HISTORY_LENGTH, FORECAST_HORIZON, START_YEAR, END_YEAR, \
    TESTING_SIZE, VALIDATION_SIZE


def main():
    data = pd.read_csv(f"{HISTORICAL_DATA_BASE_ADDRESS}/{START_YEAR}_{END_YEAR}/"
                       f"{FORECAST_HORIZON}/historical_data h={HISTORY_LENGTH}.csv")
    data.dropna(inplace=True)
    y = np.array(data[['Normal target']]).reshape(-1)
    X = np.array(data.drop(['spatial id', 'temporal id','Target (normal)', 'Normal target'], axis=1))
    print(X.shape, y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TESTING_SIZE, random_state=13)
    X_train, X_val, y_train, y_val = \
        train_test_split(X_train, y_train, test_size=VALIDATION_SIZE / (1 - TESTING_SIZE), random_state=23)
    print(X_train.shape, type(X_train))
    # KNeighborsClassifierObject = KNeighborsClassifier()
    # neighbors = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
    # neighbors = neighbors[neighbors < len(X_train) * (4 / 5)]
    # GridSearchOnKs = GridSearchCV(KNeighborsClassifierObject, param_grid={'n_neighbors': neighbors}, cv=5)
    # GridSearchOnKs.fit(X_train, y_train)
    # best_K = GridSearchOnKs.best_params_['n_neighbors']
    # print(best_K)
    # KNN_Model = KNeighborsClassifier(n_neighbors=best_K)
    # KNN_Model.fit(X_train, y_train.ravel())
    # testing_predictions = KNN_Model.predict_proba(X_testing)
    # train_predictions = KNN_Model.predict_proba(X_training)


if __name__ == '__main__':
    main()
