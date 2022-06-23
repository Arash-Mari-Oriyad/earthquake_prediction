import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(font_scale=1.1, style='white')

t_a = 'Total accuracy'
t_p_a = 'True positive accuracy'
t_n_a = 'True negative accuracy'

data_df = pd.DataFrame(data={"accuracy_type": [t_a, t_a, t_a, t_p_a, t_p_a, t_p_a, t_n_a, t_n_a, t_n_a],
                             "models": ['KNN', 'GLM', 'LSTM', 'KNN', 'GLM', 'LSTM', 'KNN', 'GLM', 'LSTM'],
                             "accuracy": [73.61, 73.3, 74.81, 79.33, 79.21, 68.56, 67.65, 67.14, 81.31]})
plt.figure(figsize=(8, 6))
plot = sns.barplot(x="models", y="accuracy", hue="accuracy_type",
                    data=data_df, palette=['#3182bd', '#9ecae1', '#deebf7'])

for p in plot.patches:
    plot.annotate(format(p.get_height()),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')

plt.ylabel("Accuracy", size=14)
plt.xlabel("", size=14)
plt.ylim(50, 90)
plt.legend()
plt.savefig('main_experiment_fig.svg', format='svg')
