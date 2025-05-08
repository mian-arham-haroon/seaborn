import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
var=[1,2,3,4,5,6]
var1=[2,3,4,5,2,1]
x1=sns.load_dataset("titanic").head(20)
print(x1)

# sns.barplot(x=x1.pclass,y=x1.age)
order=["2","1","3"]
sns.barplot(x="pclass",y="fare",data=x1,hue="who",order=order,hue_order=['child','man','woman'],ci=60,n_boot=3)

# x=pd.DataFrame({'var':var,'var1':var1})
# sns.lineplot(x='var',y='var1',data=x)
# sns.lineplot(x='age',y='pclass',data=x1,hue='sex',style='sex',palette='Accent',markers=["o",">"],dashes=False,legend='full',
            #  )
# plt.grid()
# plt.title("arham")
# sns.lineplot(x='alcohol',y='no_previous',data=x1,size=10) 
# sns.lineplot(x=var,y=var1)

# plt.plot(var,var1)
plt.show()
