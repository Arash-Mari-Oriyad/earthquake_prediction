import matplotlib.pyplot as plt

x = [x for x in range(1, 13)]
knn_accuracies = [73.61, 73.23, 71.02, 69.13, 72.51, 70.73, 71.94, 71.33, 70.60, 71.39, 71.46, 72.38]
glm_accuracies = [73.30, 72.79, 71.72, 72.03, 72.32, 72.44, 72.76, 71.46, 71.20, 71.84, 72.09, 72.19]

plt.plot(x, knn_accuracies, '--bo', label='KNN')
plt.plot(x, glm_accuracies, '--go', label='GLM')

plt.ylabel("Accuracy", size=10)
plt.xlabel("Forecast horizon (month)", size=10)
plt.xticks(x)
plt.xlim((0, 13))
plt.ylim((69, 74))
plt.legend()
plt.savefig('different_forecast_horizons_fig.svg', format='svg')
