import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
dataset = pd.read_csv(file_path)
sec_a=n.array([75,65,73,68,72,76])
sec_b=n.array([90,47,43,96,93,51])
no=n.array([1,2,3,4,5,6])
mean_a=n.mean(sec_a)
mean_b=n.mean(sec_b)
mad_a=n.sum(n.abs(sec_a-mean_a))/len(sec_a)
mad_b=n.sum(n.abs(sec_b-mean_b))/len(sec_b)
print("MAD_A:",mad_a)
print("MAD_B:",mad_b)
plt.figure(figsize=(10,5))
plt.scatter(sec_a,no,c="Blue",label="Section A")
plt.scatter(sec_b,no,c="Red",label="Section B")
plt.plot([70,70,70,70,70,70],no,c="Blue",label="Mean")
plt.legend()
plt.show()

