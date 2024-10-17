import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
dataset = pd.read_csv(file_path)
# dataset.isnull().sum()
# dataset["Age"].fillna(dataset["Age"].mean(),inplace=True)
print(n.median(dataset["Fare"]))
md=dataset["Fare"].median()
mn=dataset["Fare"].mean()
print(dataset["Fare"].median())
print(dataset["Fare"].mean())
print(sns.histplot(x="Fare",data=dataset,bins=[i for i in range(0,81,10)]))
plt.plot([md for i in range(0,300)],[i for i in range(0,300)],c='orange')
plt.plot([mn for i in range(0,300)],[i for i in range(0,300)],c='green')



