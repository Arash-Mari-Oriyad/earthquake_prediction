import pandas as pd
import matplotlib.pyplot as plt

x = [x for x in range(1, 13)]
knn_accuracies = []
glm_accuracies = []

for forecast_horizon in range(1, 13):
    knn_accuracy_df = pd.read_csv(f"../../experiments/long_range_prediction/results/knn/"
                                  f"{forecast_horizon}/performance/test process"
                                  f"/test performance report forecast horizon = {forecast_horizon}.csv")
    knn_accuracies.append(round(knn_accuracy_df["AUC"][0] * 100, 2))
    glm_accuracy_df = pd.read_csv(f"../../experiments/long_range_prediction/results/glm/"
                                  f"{forecast_horizon}/performance/test process"
                                  f"/test performance report forecast horizon = {forecast_horizon}.csv")
    glm_accuracies.append(round(glm_accuracy_df["AUC"][0] * 100, 2))

print(knn_accuracies)
print(glm_accuracies)

plt.plot(x, knn_accuracies, '--bo', label='KNN')
plt.plot(x, glm_accuracies, '--go', label='GLM')

plt.ylabel("AUC", size=10)
plt.xlabel("Forecast horizon (month)", size=10)
plt.xticks(x)
plt.xlim((0, 13))
plt.ylim((75, 80))
plt.legend()
plt.savefig('long_range_prediction_fig.png', format='png')
plt.savefig('long_range_prediction_fig.svg', format='svg')
