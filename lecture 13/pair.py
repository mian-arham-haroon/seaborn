import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd


var=sns.load_dataset("tips")
# sns.pairplot(var,hue=sex)
# sns.pairplot(var,hue="sex")
# sns.pairplot(var,vars=['total_bill','tip'],hue_order=['Female','Male'],palette='Dark2',hue="sex")
# sns.pairplot(var,hue_order=['Female','Male'],palette='Dark2',hue="sex",x_vars=['total_bill','tip'])
# sns.pairplot(var,hue_order=['Female','Male'],palette='Dark2',hue="sex",kind='reg',diag_kind='hist')
sns.pairplot(var,hue_order=['Female','Male'],palette='Dark2',hue="sex",markers=['^','*'])















plt.show()