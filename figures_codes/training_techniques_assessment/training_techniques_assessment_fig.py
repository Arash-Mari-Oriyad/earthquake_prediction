import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MODELS = ['glm', 'knn']

sns.set_theme(font_scale=1.3, style='whitegrid')

fig, ax = plt.subplots(2, 1, figsize=(1 * 8, 2 * 4), squeeze=False)

for index, model in enumerate(MODELS):
    main_experiment_accuracy = round(pd.read_csv(f"../../experiments/main_experiment/results/"
                                                 f"{model}/accuracy/testing_accuracy.csv")['accuracy'][0] * 100, 2)
    cross_validation_accuracy = round(
        pd.read_csv(f"../../experiments/training_techniques_assessment/cross_validation/"
                    f"results/{model}/accuracy/testing_accuracy.csv")['accuracy'][0] * 100, 2)
    without_historical_features = round(pd.read_csv(
        f"../../experiments/training_techniques_assessment/without_historical_features/results/{model}/"
        f"accuracy/testing_accuracy.csv")['accuracy'][0] * 100, 2)
    random_splitting = round(pd.read_csv(
        f"../../experiments/training_techniques_assessment/random_splitting/results/"
        f"{model}/accuracy/testing_accuracy.csv")['accuracy'][0] * 100, 2)
    data = {"Experiment": ['main experiment', 'without\nhistorical features', 'random splitting',
                                'cross validation'],
            "Accuracy": [main_experiment_accuracy, without_historical_features, random_splitting,
                         cross_validation_accuracy]}
    df = pd.DataFrame(data, columns=['Experiment', 'Accuracy'])
    # plt.figure(figsize=(8, 8))
    plots = sns.barplot(x="Experiment", y="Accuracy", data=df, ax=ax[index][0],
                        palette=['#3182bd', '#9ecae1', '#9ecae1', '#9ecae1'])
    for bar in plots.patches:
        plots.annotate(format(bar.get_height(), '.2f'),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=15, xytext=(0, 8),
                       textcoords='offset points')
    model_name = model.upper()
    ax[index][0].set_title(f"{model_name}", fontsize=15)
    ax[index][0].set_xlabel("", fontsize=15)
    ax[index][0].set_ylabel("Accuracy (%)", fontsize=15)
    ax[index][0].set_ylim(40, 80)
    # plt.xlabel("", size=15)
    # plt.ylabel("Accuracy", size=15)

plt.tight_layout()
plt.savefig(f'training_techniques_assessment_fig.png', format='png')
plt.savefig(f'training_techniques_assessment_fig.svg', format='svg')
