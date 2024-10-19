import pandas as pd
import numpy as np
import   matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("tip.csv")
dataset.info()
data_corr=dataset.select_dtypes({"float64","int64"}).corr()
data_cov=dataset.select_dtypes({"float64","int64"}).cov()
sns.heatmap(data_corr,annot=True)

plt.show()
sns.heatmap(data_cov,annot=True)
plt.show()