import seaborn as sns
import matplotlib.pyplot as plt


f=sns.load_dataset("tips")

sns.set(style='whitegrid')
# sns.boxplot(x='day',y='total_bill',data=f,hue='sex',color='r')
# sns.boxplot(y='day',x='total_bill',data=f,hue='sex',order=['Fri','Sun','Sat','Thur'],showmeans=True
            # ,meanprops={"marker":"*","markeredgecolor":'k','markerfacecolor':'w'},palette='Accent')
# sns.boxplot(data=f,showmeans=True
#             ,meanprops={"marker":"*","markeredgecolor":'k','markerfacecolor':'w'},palette='Accent',orient='h',)
# sns.boxplot(x=f['total_bill'])














plt.show()