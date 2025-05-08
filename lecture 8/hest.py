import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

var=np.linspace(1,10,20).reshape(4,5)


x1=sns.load_dataset("car_crashes").head(20)
v=x1.drop(columns=["ins_losses","abbrev","ins_premium","not_distracted"],axis=1).head(10)
print(v)



sns.heatmap(v,vmin=0,vmax=20,cmap='Dark2')



plt.show() 