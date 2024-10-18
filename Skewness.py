import pandas as pd
import numpy as np
import   matplotlib.pyplot as plt
import seaborn as sns
# data=np .random.normal(0,100,100)
#print(data)
data=[2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]
df=pd.DataFrame({'x':data})
df['x'].skew()
sns.histplot(x='x',data=df,color="darkblue",bins=[2,3,4,5,6,7,8,9,10,11,12])
plt.show()
dataset=pd.read_csv("titanic.csv")
#sns.histplot(x="Age",data=dataset)
#plt.show()  