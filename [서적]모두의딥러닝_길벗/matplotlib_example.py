import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

df = pd.read_csv('../dataset/pima-indians-diabetes.csv',
                 names=["pregant", "plasma", "pressure", "thickness",
                        "insulin", "BMI", "pedigree", "age", "class"])

plt.figure(figsize=(12, 12))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()

grid=sns.FacetGrid(df,col='class')
grid.map(plt.hist,'plasma',bins=10)
plt.show()
