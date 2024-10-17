import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
df = pd.read_csv(file_path)
mean=n.mean(df["Age"])
print(df["Age"].mean())
print(mean)
print(sns.histplot(x="Age",data=df,bins=[i for i in range(0,81,10)]))
plt.plot([mean for i in range(0,300)],[i for i in range(0,300)],c='red')


