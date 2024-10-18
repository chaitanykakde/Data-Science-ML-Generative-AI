import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("titanic.csv")
dataset['Age'].fillna(dataset["Age"].mean(),inplace=Ture)
