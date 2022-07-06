import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = ['Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov',
     'Dec', 'Jan', 'Feb', 'Mar']
s_r_1 = [77, 71.7, 71.5, 81.5, 80, 77.9, 79.4, 81.9, 78.3, 82, 82.5, 63.1]
s_r_2 = [85.5, 73.3, 84, 72, 72.5, 82.1, 83.8, 78.8, 72.5, 83.5, 81.9, 73.1]
s_r_3 = [53, 49.2, 33.5, 45, 41.3, 58.6, 45, 59.4, 50, 29.5, 55.6, 44.4]
s_r_4 = [78, 74.2, 76, 72.5, 71.3, 71.4, 69.4, 69.4, 65.8, 76, 70, 61.3]
s_r_5 = [85, 80.8, 85, 82.5, 82.5, 87.1, 87.5, 85, 85, 82, 85.6, 71.9]
s_r_6 = [87, 87.5, 85.5, 82.5, 87.5, 85.7, 84.4, 84.4, 86.7, 85.5, 85.6, 84.4]
s_r_7 = [2, 1.7, 2, 2, 1.3, 1.4, 2.5, 2.5, 1.7, 2.5, 2.5, 3.1]
s_r_8 = [17, 16.7, 22.5, 18, 26.3, 15, 13.1, 23.1, 20.8, 21, 14.4, 16.3]
s_r_9 = [19.5, 29.2, 19, 44.5, 27.5, 30, 16.9, 22.5, 27.5, 23, 20, 25]
s_r_predictions = [s_r_1, s_r_2, s_r_3, s_r_4, s_r_5, s_r_6, s_r_7, s_r_8, s_r_9]

fig, ax = plt.subplots(3, 3)

for i in range(3):
    for j in range(3):
        ax[i][j].plot(x, s_r_predictions[3 * i + j], '--bo', linewidth=0.1, markersize=2)
        ax[i][j].set_title(f'subregion {3 * i + j + 1}', fontsize=8)
        ax[i][j].tick_params(axis='y', labelsize=6)
        ax[i][j].set_xticklabels(labels=x, rotation=90, fontsize=6)
        f = np.floor(min(s_r_predictions[3 * i + j]))
        c = np.ceil(max(s_r_predictions[3 * i + j]))
        ax[i][j].set_yticks(np.arange(f,
                                      c,
                                      1 if c - f <= 5 else (2 if c - f <= 10 else 5)))
fig.subplots_adjust(wspace=0.5, hspace=0.75)
fig.savefig('earthquake_forecasting_fig.png', format='png')
