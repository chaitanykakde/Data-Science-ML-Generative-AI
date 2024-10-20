import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Generate population data
pop_data = [np.random.randint(10, 100) for i in range(10000)]
pd_table = pd.DataFrame({"Pop_data": pop_data})

# Plot population data
sns.kdeplot(x="Pop_data", data=pd_table)
plt.show()

# Sample means
sam_mean = []
for no_sample in range(60):
    sample_data = []
    for data in range(500):
        sample_data.append(np.random.choice(pop_data))
    sam_mean.append(np.mean(sample_data))

# Create DataFrame for sample means
sam_M = pd.DataFrame({"Sample_Mean": sam_mean})

# Plot sample means
sns.kdeplot(x="Sample_Mean", data=sam_M)
plt.show()
