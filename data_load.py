from pandas import read_csv

# Load dataset
fl = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(fl, names=names)

#Dropping data with missing values
dataset.dropna(axis=0, how='any')
#printing the rows and columns of the data set
print(dataset.shape)
#Taking a peek at he data
print(dataset.head(20))
#printing the statistical descriptions like mean,std,etc
print(dataset.describe())
#Show number of data sets of each class
print(dataset.groupby('class').size())
	

