import matplotlib.pyplot as plt
import seaborn as sns


var=sns.load_dataset('tips')
plt.figure(figsize=(3,5))
sns.set_context('poster',font_scale=1)
# sns.set('paper')
sns.set_style('whitegrid')
# sns.boxplot(y=var['total_bill'])
sns.barplot(x='day',y='total_bill',data=var)
# plt.grid()
sns.despine()











plt.show()