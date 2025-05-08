import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd


var=sns.load_dataset("tips")
# sns.violinplot(x="day",y="total_bill",data=var,palette='Dark2',linewidth=2)
# sns.violinplot(x="day",y="total_bill",saturation=0.9,data=var,palette='Dark2',order=["Dinner","Lunch"])
# sns.violinplot(x="day",y="total_bill",saturation=0.9,data=var,palette='Dark2',hue="sex",split=True,scale='area')
# sns.violinplot(x="total_bill",y="day",saturation=0.9,data=var,palette='Dark2',hue="sex",split=True,scale='area',inner="quart")
sns.violinplot(x=var["total_bill"])





















plt.show()