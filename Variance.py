import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
dataset = pd.read_csv(file_path)
sec_a=n.array([75,65,73,68,72,76])
sec_b=n.array([90,47,43,96,93,51])
no=n.array([1,2,3,4,5,6])
var_a=n.var(sec_a)
var_b=n.var(sec_b)
print("var A:",var_a)
print("var B:",var_b)
var_age=dataset["Age"].var()
print("Variance:",var_age)
sns.histplot(x="Age",data=dataset,color="Red")
dataset.describe()

