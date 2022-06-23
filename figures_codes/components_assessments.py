import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(font_scale=1.3, style='whitegrid')


data = {"experiment_type": ['main experiment', 'without\nhistorical features', 'random splitting', 'cross validation'],
        "accuracy": [73.61, 67.59, 51.32, 73.17]}

df = pd.DataFrame(data, columns=['experiment_type', 'accuracy'])

plt.figure(figsize=(8, 8))
plots = sns.barplot(x="experiment_type", y="accuracy", data=df, palette=['#3182bd', '#9ecae1', '#9ecae1', '#9ecae1'])

for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 8),
                   textcoords='offset points')
# plots

plt.xlabel("", size=15)
plt.ylabel("Accuracy", size=15)
plt.savefig('components_assessments.svg', format='svg')
