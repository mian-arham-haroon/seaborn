import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x1=sns.load_dataset("tips")
print(x1)
sns.countplot(y="sex",palette='Dark2',saturation=0.9,data=x1,hue="smoker")












plt.show()
