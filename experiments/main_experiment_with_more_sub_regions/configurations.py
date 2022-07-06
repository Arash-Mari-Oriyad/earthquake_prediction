HISTORY_LENGTHS = [i for i in range(1, 13)]
FORECAST_HORIZON = 1
START_YEAR, END_YEAR = 1966, 2016
N_HORIZONTAL, N_VERTICAL = 5, 5
GROUPING_PLAN = False

VALIDATION_SIZE = 0.3
TESTING_SIZE = 0.3

MODELS = ["knn", "glm"]

HISTORICAL_DATA_BASE_ADDRESS = f"../../data/historical_data/{START_YEAR}_{END_YEAR}/{N_HORIZONTAL}_{N_VERTICAL}/" \
                               f"{'with_grouping_plan' if GROUPING_PLAN else 'without_grouping_plan'}"
RESULTS_BASE_ADDRESS = "results"
VALIDATION_PREDICTIONS_BASE_ADDRESS = "prediction/validation process"
TESTING_PREDICTIONS_BASE_ADDRESS = "prediction/test process"

INF = pow(10, 12)
