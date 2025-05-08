import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
var=[1,2,3,4,5,6]
var1=[2,3,4,5,2,1]
x1=sns.load_dataset("titanic").head(20)
print(x1)
# sns.set(style='darkgrid')
sns.barplot(x=x1.pclass,y=x1.age,errcolor='k',saturation=100,hue=x1.sex,errwidth=2,capsize=0,dodge='f')
order=["2","1","3"]
# sns.barplot(x="pclass",y="fare",data=x1,orient='h',hue="who",order=order,hue_order=['child','man','woman'],color='k',palette='Dark2',saturation=2)

# x=pd.DataFrame({'var':var,'var1':var1})
# sns.lineplot(x='var',y='var1',data=x)
# sns.lineplot(x='age',y='pclass',data=x1,hue='sex',style='sex',palette='Accent',markers=["o",">"],ci=60,n_boot=3,dashes=False,legend='full',
#              )
# plt.grid()
# plt.title("arham")
# sns.lineplot(x='alcohol',y='no_previous',data=x1,size=10) 
# sns.lineplot(x=var,y=var1)

# plt.plot(var,var1)
plt.show() 
