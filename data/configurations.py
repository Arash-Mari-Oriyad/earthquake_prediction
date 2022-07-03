import datetime


START_DATE = datetime.date(year=1966, month=10, day=1)
END_DATE = datetime.date(year=2016, month=9, day=30)

START_LONGITUDE, END_LONGITUDE = 75, 119
START_LATITUDE, END_LATITUDE = 23, 45
N_HORIZONTAL, N_VERTICAL = 3, 3

MAXIMUM_HISTORY_LENGTH = 12
FORECAST_HORIZONS = [i for i in range(1, 13)]
TEMPORAL_COLUMN_NAME = "month ID"
SPATIAL_COLUMN_NAME = "sub-region ID"
TEMPORAL_COVARIATES = ["occurrence"]
TARGET = "occurrence"

RAW_DATA_ADDRESS = f"raw_data/{START_DATE.year}_{END_DATE.year}/raw_data.csv"
TRANSFORMED_DATA_ADDRESS = f"transformed_data/{START_DATE.year}_{END_DATE.year}/transformed_data.csv"
HISTORICAL_DATA_BASE_ADDRESS = f"historical_data/{START_DATE.year}_{END_DATE.year}"
