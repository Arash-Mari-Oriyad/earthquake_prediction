import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

GROUPS = [[1, 2, 5, 6], [4, 7, 8, 9], [3]]
number_of_sub_regions = sum([len(group) for group in GROUPS])

sns.set_theme(font_scale=0.8, style='white')

t_a = 'Total accuracy'
f_g_a = 'First group accuracy'
s_g_a = 'Second group accuracy'
t_g_a = 'Third group accuracy'

accuracies = []

total_accuracy = 0
group_accuracies = []
for group in GROUPS:
    knn_accuracy_df = pd.read_csv(f'../../experiments/main_experiment_with_grouping_plan/results/knn/'
                                  f'{"_".join([str(s_r) for s_r in group])}/accuracy/testing_accuracy.csv')
    total_accuracy += len(group) * round(knn_accuracy_df["accuracy"][0] * 100, 2)
    group_accuracies.append(round(knn_accuracy_df["accuracy"][0] * 100, 2))
accuracies.append(round(total_accuracy/number_of_sub_regions, 2))
for group_accuracy in group_accuracies:
    accuracies.append(group_accuracy)

total_accuracy = 0
group_accuracies = []
for group in GROUPS:
    glm_accuracy_df = pd.read_csv(f'../../experiments/main_experiment_with_grouping_plan/results/glm/'
                                  f'{"_".join([str(s_r) for s_r in group])}/accuracy/testing_accuracy.csv')
    total_accuracy += len(group) * round(glm_accuracy_df["accuracy"][0] * 100, 2)
    group_accuracies.append(round(glm_accuracy_df["accuracy"][0] * 100, 2))
accuracies.append(round(total_accuracy/number_of_sub_regions, 2))
for group_accuracy in group_accuracies:
    accuracies.append(group_accuracy)

accuracies.append(85.12)
accuracies.append(88.57)
accuracies.append(87.57)
accuracies.append(61.6)

data_df = pd.DataFrame(data={"accuracy_type":
                                 [t_a, f_g_a, s_g_a, t_g_a, t_a, f_g_a, s_g_a, t_g_a, t_a, f_g_a, s_g_a, t_g_a],
                             "models":
                                 ['KNN', 'KNN', 'KNN', 'KNN', 'GLM', 'GLM', 'GLM', 'GLM',
                                  'LSTM', 'LSTM', 'LSTM', 'LSTM'],
                             "accuracy": accuracies})
plt.figure(figsize=(8, 6))
plot = sns.barplot(x="models", y="accuracy", hue="accuracy_type",
                    data=data_df, palette=['#115282', '#3182bd', '#9ecae1', '#deebf7'])

for p in plot.patches:
    plot.annotate(format(p.get_height()),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')

plt.ylabel("Accuracy", size=14)
plt.xlabel("Model", size=14)
plt.ylim(20, 100)
plt.legend()
plt.savefig('main_experiment_with_grouping_plan_fig.png', format='png')
plt.savefig('main_experiment_with_grouping_plan_fig.svg', format='svg')
