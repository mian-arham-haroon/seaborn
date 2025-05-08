import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# var=np.linspace(1,10,20).reshape(4,5)
var=np.linspace(1,10,10).reshape(2,5)


x1=sns.load_dataset("car_crashes").head(20)
v=x1.drop(columns=["ins_losses","abbrev","ins_premium","not_distracted"],axis=1).head(10)
# print(v)


y={"fontsize":20,'color':'k'}
# sns.heatmap(var,vmin=0,vmax=20,cmap='Dark2',annot=True)
sns.set(font_scale=2)
ar=np.array([['a0','a1','a2','a3','a4'],['B0','B1','B2','B3','B4']])
v=sns.heatmap(var,vmin=0,vmax=20,cmap='Dark2',annot=ar,fmt='s',annot_kws=y,linewidths=4,linecolor='k',cbar=False,xticklabels=False,yticklabels=False)
v.set(xlabel="arham",ylabel="haroon")
plt.show() 