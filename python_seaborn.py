import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#stats = pd.read_excel('C:\\Siri F1 assignments\\Dinesh anna\\Journalist Deaths (1).xlsx')
stats = pd.read_excel('C:\Siri F1 assignments\SEC 6050\week3\data_visualization.xlsx')
print(stats)
print(stats.head())
vis = sns.distplot(stats['Year'])
plt.show()
#to see bins
vis = sns.distplot(stats['Year'],bins=10)
plt.show()
vis2 = sns.boxplot(data=stats,x='Year',y='AvrgMax')
plt.show()
#linear model
vis3 = sns.lmplot(data=stats,x='AvrgMax',y='Year',fit_reg=False,hue='AvrgMax',scatter_kws={'s':100}) #hue is for color
plt.show()
