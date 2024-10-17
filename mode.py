import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
dataset = pd.read_csv(file_path)
print(n.median(dataset["Fare"]))
md=dataset["Fare"].median()
mn=dataset["Fare"].mean()
mode=dataset["Fare"].mode()
print("Median:",dataset["Fare"].median())
print("Mean:",dataset["Fare"].mean())
print("Mode:",dataset["Fare"].mode())
print(sns.histplot(x="Fare",data=dataset,bins=[i for i in range(0,81,10)]))
plt.plot([md for i in range(0,300)],[i for i in range(0,300)],c='orange',label="Median")
plt.plot([mn for i in range(0,300)],[i for i in range(0,300)],c='green',label="Mean")
plt.plot([mode for i in range(0,300)],[i for i in range(0,300)],c='red',label="Mode")
plt.legend()
plt.show()



