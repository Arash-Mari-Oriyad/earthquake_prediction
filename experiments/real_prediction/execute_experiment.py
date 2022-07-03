import os
import shutil

import stpredict

from configurations import HISTORICAL_DATA_BASE_ADDRESS, START_YEAR, END_YEAR, FORECAST_HORIZONS, HISTORY_LENGTHS, \
    MODELS, RESULTS_BASE_ADDRESS, VALIDATION_SIZE, TESTING_SIZE


def main():
    for forecast_horizon in FORECAST_HORIZONS:
        input_data_addresses = \
            [f"{HISTORICAL_DATA_BASE_ADDRESS}/{START_YEAR}_{END_YEAR}/{forecast_horizon}/historical_data h={h}.csv"
             for h in HISTORY_LENGTHS]
        for model in MODELS:
            stpredict.whole_as_one(data=input_data_addresses,
                                   forecast_horizon=forecast_horizon,
                                   feature_sets={'feature': 'mRMR'},
                                   model_type='classification',
                                   models=[model],
                                   splitting_type='training-validation',
                                   instance_testing_size=TESTING_SIZE,
                                   instance_validation_size=VALIDATION_SIZE,
                                   performance_benchmark='AUC',
                                   performance_measures=['AUC', 'likelihood', 'AUPR'],
                                   validation_performance_report=True,
                                   testing_performance_report=True,
                                   save_ranked_features=True,
                                   save_predictions=True,
                                   verbose=1)
            results_address = f"{RESULTS_BASE_ADDRESS}/{model}/{forecast_horizon}/"
            if os.path.exists(results_address):
                shutil.rmtree(results_address)
            os.makedirs(results_address)
            shutil.move("prediction", results_address)
    return


if __name__ == "__main__":
    main()
