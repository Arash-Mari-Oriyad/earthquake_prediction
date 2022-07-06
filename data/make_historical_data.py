import stpredict
import pandas as pd

from configurations import MAXIMUM_HISTORY_LENGTH, FORECAST_HORIZONS, TEMPORAL_COVARIATES, TEMPORAL_COLUMN_NAME, \
    SPATIAL_COLUMN_NAME, TARGET, TRANSFORMED_DATA_BASE_ADDRESS, HISTORICAL_DATA_BASE_ADDRESS, GROUPS, GROUPING_PLAN


def main():
    print("Historical data making process is started!")

    temporal_covariates_maximum_history_length = {temporal_covariate: MAXIMUM_HISTORY_LENGTH
                                                  for temporal_covariate in TEMPORAL_COVARIATES}
    column_identifier = {"temporal id level 1": TEMPORAL_COLUMN_NAME,
                         "spatial id level 1": SPATIAL_COLUMN_NAME,
                         "temporal covariates": TEMPORAL_COVARIATES,
                         "spatial covariates": [],
                         "target": TARGET}
    if GROUPING_PLAN:
        for group in GROUPS:
            print(f"group: {group}")
            transformed_data = pd.read_csv(TRANSFORMED_DATA_BASE_ADDRESS +
                                              f"/{'_'.join([str(sub_region_id) for sub_region_id in group])}"
                                              f"/transformed_data.csv")
            for forecast_horizon in FORECAST_HORIZONS:
                print(f"forecast horizon = {forecast_horizon}")
                historical_data_address = f"{HISTORICAL_DATA_BASE_ADDRESS}/" \
                                          f"{'_'.join([str(sub_region_id) for sub_region_id in group])}/" \
                                          f"{forecast_horizon}/"
                stpredict.preprocess.preprocess_data(data=transformed_data,
                                                     forecast_horizon=forecast_horizon,
                                                     history_length=temporal_covariates_maximum_history_length,
                                                     column_identifier=column_identifier,
                                                     spatial_scale_level=1,
                                                     temporal_scale_level=1,
                                                     target_mode="normal",
                                                     imputation=False,
                                                     save_address=historical_data_address,
                                                     verbose=0)
    else:
        transformed_data = pd.read_csv(TRANSFORMED_DATA_BASE_ADDRESS + '/transformed_data.csv')
        for forecast_horizon in FORECAST_HORIZONS:
            print(f"forecast horizon = {forecast_horizon}")
            historical_data_address = f"{HISTORICAL_DATA_BASE_ADDRESS}/{forecast_horizon}/"
            stpredict.preprocess.preprocess_data(data=transformed_data,
                                                 forecast_horizon=forecast_horizon,
                                                 history_length=temporal_covariates_maximum_history_length,
                                                 column_identifier=column_identifier,
                                                 spatial_scale_level=1,
                                                 temporal_scale_level=1,
                                                 target_mode="normal",
                                                 imputation=False,
                                                 save_address=historical_data_address,
                                                 verbose=0)
    print("Historical data making process is finished!")
    return


if __name__ == "__main__":
    main()
