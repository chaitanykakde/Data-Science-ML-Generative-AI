import pandas as pd
import numpy as np
import   matplotlib.pyplot as plt
import seaborn as sns


s_x=90 
p_u=82
p_std=20
n=81
z_cal=(s_x-p_u)/(p_std/np.sqrt(n))
print(z_cal)
z_form_table=1.64
if z_cal>z_form_table:
    print("Ha is write")
else:
    print("Ho is right")   