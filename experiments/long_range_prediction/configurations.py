HISTORY_LENGTHS = [i for i in range(1, 13)]
FORECAST_HORIZONS = [i for i in range(1, 12)]
START_YEAR, END_YEAR = 1966, 2016

VALIDATION_SIZE = 0.3
TESTING_SIZE = 0.3

MODELS = ["knn", "glm"]
# MODELS = ["knn"]

HISTORICAL_DATA_BASE_ADDRESS = "../../data/historical_data"
RESULTS_BASE_ADDRESS = "results"
VALIDATION_PREDICTIONS_BASE_ADDRESS = "prediction/validation process"
TESTING_PREDICTIONS_BASE_ADDRESS = "prediction/test process"

INF = pow(10, 12)
