import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
dataset = pd.read_csv(file_path)
sec_a=n.array([75,65,73,68,72,76])
sec_b=n.array([90,47,43,96,93,51])
no=n.array([1,2,3,4,5,6])
std_a=n.std(sec_a)
std_b=n.std(sec_b)
print("STD A:",std_a)
print("STD B:",std_b)
std_age=dataset["Age"].std()
print("standard deviation:",std_age)
sns.histplot(x="Age",data=dataset,color="Green")
dataset.describe()


