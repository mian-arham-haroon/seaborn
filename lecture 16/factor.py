import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var=sns.load_dataset("tips")
sns.catplot(x='size',y='tip',data=var,kind='point',hue='sex')















plt.show()