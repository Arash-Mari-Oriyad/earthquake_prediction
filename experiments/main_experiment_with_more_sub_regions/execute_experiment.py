import os
import shutil

import stpredict

from configurations import HISTORICAL_DATA_BASE_ADDRESS, START_YEAR, END_YEAR, FORECAST_HORIZON, HISTORY_LENGTHS, \
    MODELS, RESULTS_BASE_ADDRESS, VALIDATION_SIZE, TESTING_SIZE


def main():
    input_data_addresses = \
        [f"/{FORECAST_HORIZON}/historical_data h={h}.csv"
         for h in HISTORY_LENGTHS]
    for model in MODELS:
        stpredict.whole_as_one(data=input_data_addresses,
                               forecast_horizon=FORECAST_HORIZON,
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
        results_address = f"{RESULTS_BASE_ADDRESS}/{model}/"
        if os.path.exists(results_address):
            shutil.rmtree(results_address)
        os.makedirs(results_address)
        shutil.move("prediction", results_address)
        shutil.move("performance", results_address)
        shutil.move("plots", results_address)
        shutil.move("ranked features", results_address)
    return


if __name__ == "__main__":
    main()
