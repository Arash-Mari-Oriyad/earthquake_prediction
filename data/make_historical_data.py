import stpredict
import pandas as pd


def main():
    transformed_data_address = 'transformed_data/1966_2016/transformed_data.csv'
    maximum_history_length = 12
    temporal_covariates = ['occurrence']
    target = 'occurrence'
    transformed_data = pd.read_csv(transformed_data_address)
    temporal_covariates_maximum_history_length = {temporal_covariate: maximum_history_length
                                                  for temporal_covariate in temporal_covariates}
    column_identifier = {'temporal id level 1': 'month ID',
                         'spatial id level 1': 'sub-region ID',
                         'temporal covariates': temporal_covariates,
                         'spatial covariates': [],
                         'target': target}

    for forecast_horizon in range(1, 13):
        historical_data_address = f'historical_data/1966_2016/{forecast_horizon}/'
        stpredict.preprocess.preprocess_data(data=transformed_data,
                                             forecast_horizon=forecast_horizon,
                                             history_length=temporal_covariates_maximum_history_length,
                                             column_identifier=column_identifier,
                                             spatial_scale_level=1,
                                             temporal_scale_level=1,
                                             target_mode='normal',
                                             imputation=False,
                                             save_address=historical_data_address,
                                             verbose=0)


if __name__ == '__main__':
    main()
