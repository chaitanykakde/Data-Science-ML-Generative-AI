import pandas as pd
import numpy as np
import   matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("titanic.csv")
dataset['Age'].fillna(dataset["Age"].mean(),inplace=True)
print(np.percentile(dataset['Age'],50),np.percentile(dataset['Age'],100))
print(dataset['Age'].min())
print(dataset['Age'].max())
print(dataset['Age'].median())
sns.boxplot(x='Fare',data=dataset,color='green')
plt.how()    