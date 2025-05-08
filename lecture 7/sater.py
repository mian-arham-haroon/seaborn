import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var=[1,2,3,4,5,6]
var1=[2,3,4,5,2,1]
x={"man":"*","woman":">","child":"o"}
x1=sns.load_dataset("titanic").head(30)
print(x1)
sns.scatterplot(x='age',y='fare',data=x1,hue='who',size='who',sizes=(10,200),palette='Dark2',style='who',markers=x)





plt.show() 