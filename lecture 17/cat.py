import matplotlib.pyplot as plt
import seaborn as sns
import pandas




var=sns.load_dataset('tips')
sns.catplot(x='tip',y='size',data=var,height=7,palette='Dark2',kind='bar')














plt.show()