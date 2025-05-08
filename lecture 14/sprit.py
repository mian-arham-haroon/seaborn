import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

var=sns.load_dataset("tips")
m={"Male":"<","Female":"o"}
# sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='Dark2',linewidth=0.2,edgecolor='k',jitter=0.3,size=10,
#               marker="v",alpha=0.6)

# sns.stripplot(x=var["total_bill"])
sns.stripplot(y=var["total_bill"])

















plt.show()