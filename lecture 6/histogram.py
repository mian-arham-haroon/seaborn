import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
var=[1,2,3,4,5,6]
var1=[2,3,4,5,2,1]
x1=sns.load_dataset("titanic")
print(x1)
sns.displot(x1["age"],bins=[0,18,35,50,80],kde=True,rug=True,color='r',log_scale=True)




plt.show() 
