from pandas import read_csv
from matplotlib import pyplot
import numpy as np
import seaborn as sns

# Loading dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
dataset.dropna(axis=0, how='any')	

#using seaborn to visualize the data

sns.set(style="ticks")
sns.pairplot(dataset,hue="class")
pyplot.show()

