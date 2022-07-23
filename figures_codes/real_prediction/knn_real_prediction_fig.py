import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = ['July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr',
 'May', 'June']
sub_regions_predictions = [[] for _ in range(9)]

for forecast_horizon in range(1, 13):
    testing_predictions_address = f"../../experiments/real_prediction/results/knn/{forecast_horizon}/prediction/future prediction/future prediction forecast horizon = {forecast_horizon}.csv"
    testing_predictions_df = pd.read_csv(testing_predictions_address)

    for s_r in range(1, 10):
        sub_regions_predictions[s_r-1].append(round(testing_predictions_df.loc[(testing_predictions_df['spatial id']==s_r) & (testing_predictions_df['temporal id']==f'669+{forecast_horizon}'), 'class 1'].tolist()[0] * 100, 2))

for s_r in range(9):
    print(sub_regions_predictions[s_r])

fig, ax = plt.subplots(3, 3)

for i in range(3):
    for j in range(3):
        ax[i][j].plot(x, sub_regions_predictions[3 * i + j], '--bo', linewidth=0.1, markersize=2)
        ax[i][j].set_title(f'subregion {3 * i + j + 1}', fontsize=8)
        ax[i][j].tick_params(axis='y', labelsize=6)
        ax[i][j].set_xticklabels(labels=x, rotation=90, fontsize=6)
        f = np.floor(min(sub_regions_predictions[3 * i + j]))
        c = np.ceil(max(sub_regions_predictions[3 * i + j]))
        ax[i][j].set_yticks(np.arange(f,
                                      c,
                                      1 if c - f <= 5 else (2 if c - f <= 10 else 5 if c -f <=40 else 10)))
fig.subplots_adjust(wspace=0.5, hspace=0.75)
fig.savefig('knn_real_prediction_fig.png', format='png')
fig.savefig('knn_real_prediction_fig.svg', format='svg')
