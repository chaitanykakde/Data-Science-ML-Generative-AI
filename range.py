import pandas as pd
import numpy as n
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "titanic.csv"
dataset = pd.read_csv(file_path)
min_r=dataset["Age"].min()
max_r=dataset["Age"].max()
print("Min:",min_r)
print("Max:",max_r)
range=max_r-min_r
print("Range:",range)
