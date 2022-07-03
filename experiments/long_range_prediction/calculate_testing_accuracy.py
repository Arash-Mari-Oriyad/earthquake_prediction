import os
import shutil
from collections import Counter

import pandas as pd

from configurations import VALIDATION_PREDICTIONS_BASE_ADDRESS, TESTING_PREDICTIONS_BASE_ADDRESS, RESULTS_BASE_ADDRESS,\
    MODELS, FORECAST_HORIZONS, INF


def calculate_accuracy(prediction_data, threshold):
    n_samples = prediction_data.shape[0]
    prediction_data['new'] = 0
    prediction_data.loc[(prediction_data['real'] == 1) & (prediction_data['class 1'] >= threshold), 'new'] = 1
    prediction_data.loc[(prediction_data['real'] == 0) & (prediction_data['class 1'] < threshold), 'new'] = 1
    return prediction_data['new'].sum() / n_samples


def calculate_true_positive_rate(prediction_data, threshold):
    prediction_data['new'] = 0
    prediction_data.loc[(prediction_data['real'] == 1) & (prediction_data['class 1'] >= threshold), 'new'] = 1
    return prediction_data['new'].sum() / prediction_data['real'].sum()


def calculate_true_negative_rate(prediction_data, threshold):
    n_samples = prediction_data.shape[0]
    prediction_data['new'] = 0
    prediction_data.loc[(prediction_data['real'] == 0) & (prediction_data['class 1'] < threshold), 'new'] = 1
    return prediction_data['new'].sum() / (n_samples - prediction_data['real'].sum())


def exhaustive_search(predictions_df):
    Y_hat = predictions_df['class 1'].to_numpy()
    thresholds = set(Y_hat)
    thresholds.add(0)
    thresholds.add(1)
    optimal_accuracy = -INF
    optimal_threshold = None
    for threshold in thresholds:
        accuracy = calculate_accuracy(predictions_df.copy(), threshold)
        if accuracy >= optimal_accuracy:
            optimal_accuracy = accuracy
            optimal_threshold = threshold
    return optimal_threshold


def main():
    for forecast_horizon in FORECAST_HORIZONS:
        for model in MODELS:
            validation_predictions_address = f"{RESULTS_BASE_ADDRESS}/{model}/{forecast_horizon}/" \
                                             f"{VALIDATION_PREDICTIONS_BASE_ADDRESS}/" \
                                             f"validation prediction forecast horizon = {forecast_horizon}.csv"
            validation_predictions_df = pd.read_csv(validation_predictions_address)[["real", "class 1"]]
            optimal_threshold = exhaustive_search(validation_predictions_df)
            validation_accuracy = calculate_accuracy(validation_predictions_df.copy(), optimal_threshold)
            validation_true_positive_rate = \
                calculate_true_positive_rate(validation_predictions_df.copy(), optimal_threshold)
            validation_true_negative_rate = \
                calculate_true_negative_rate(validation_predictions_df.copy(), optimal_threshold)
            testing_predictions_address = f"{RESULTS_BASE_ADDRESS}/{model}/{forecast_horizon}/" \
                                          f"{TESTING_PREDICTIONS_BASE_ADDRESS}/" \
                                             f"test prediction forecast horizon = {forecast_horizon}.csv"
            testing_predictions_df = pd.read_csv(testing_predictions_address)[["real", "class 1"]]
            testing_accuracy = calculate_accuracy(testing_predictions_df.copy(), optimal_threshold)
            testing_true_positive_rate = \
                calculate_true_positive_rate(testing_predictions_df.copy(), optimal_threshold)
            testing_true_negative_rate = \
                calculate_true_negative_rate(testing_predictions_df.copy(), optimal_threshold)
            validation_accuracy_df = pd.DataFrame(data={"accuracy": [validation_accuracy],
                                                        "true positive rate": [validation_true_positive_rate],
                                                        "true negative rate": [validation_true_negative_rate],
                                                        "optimal threshold": [optimal_threshold]})
            testing_accuracy_df = pd.DataFrame(data={"accuracy": [testing_accuracy],
                                                     "true positive rate": [testing_true_positive_rate],
                                                     "true negative rate": [testing_true_negative_rate],
                                                     "optimal threshold": [optimal_threshold]})
            accuracy_address = f"{RESULTS_BASE_ADDRESS}/{model}/{forecast_horizon}/accuracy/"
            if os.path.exists(accuracy_address):
                shutil.rmtree(accuracy_address)
            os.makedirs(accuracy_address)
            validation_accuracy_df.to_csv(f"{accuracy_address}validation_accuracy.csv", index=False)
            testing_accuracy_df.to_csv(f"{accuracy_address}testing_accuracy.csv", index=False)
    return


if __name__ == '__main__':
    main()
