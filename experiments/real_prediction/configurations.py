HISTORY_LENGTHS = [i for i in range(1, 13)]
FORECAST_HORIZONS = [i for i in range(1, 13)]
START_YEAR, END_YEAR = 1966, 2022

VALIDATION_SIZE = 0.3
TESTING_SIZE = 0.3

MODELS = ["knn", "glm"]

HISTORICAL_DATA_BASE_ADDRESS = "../../data/historical_data"
RESULTS_BASE_ADDRESS = "results"

INF = pow(10, 12)
