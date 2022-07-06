import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(font_scale=1.1, style='white')

t_a = 'Total accuracy'
t_p_a = 'True positive accuracy'
t_n_a = 'True negative accuracy'

accuracies = []

knn_accuracy_df = pd.read_csv('../../experiments/main_experiment/results/knn/accuracy/testing_accuracy.csv')
accuracies.append(round(knn_accuracy_df["accuracy"][0] * 100, 2))
accuracies.append(round(knn_accuracy_df["true positive rate"][0] * 100, 2))
accuracies.append(round(knn_accuracy_df["true negative rate"][0] * 100, 2))

glm_accuracy_df = pd.read_csv('../../experiments/main_experiment/results/glm/accuracy/testing_accuracy.csv')
accuracies.append(round(glm_accuracy_df["accuracy"][0] * 100, 2))
accuracies.append(round(glm_accuracy_df["true positive rate"][0] * 100, 2))
accuracies.append(round(glm_accuracy_df["true negative rate"][0] * 100, 2))

accuracies.append(74.81)
accuracies.append(68.56)
accuracies.append(81.31)

data_df = pd.DataFrame(data={"accuracy_type": [t_a, t_p_a, t_n_a, t_a, t_p_a, t_n_a, t_a, t_p_a, t_n_a],
                             "models": ['KNN', 'KNN', 'KNN', 'GLM', 'GLM', 'GLM', 'LSTM', 'LSTM', 'LSTM'],
                             "accuracy": accuracies})
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
plt.xlabel("Model", size=14)
plt.ylim(50, 100)
plt.legend()
plt.savefig('main_experiment_fig.png', format='png')
plt.savefig('main_experiment_fig.svg', format='svg')
