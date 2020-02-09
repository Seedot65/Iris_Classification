from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pickle as pkl
import numpy as np

# Load dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
dataset.dropna(axis=0, how='any')

#Splitting the dataset into training and validating sets
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

#Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
	
# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

#storing the model
saved_model = pkl.dumps(model)

#Loading frm pickled model
loaded_model=pkl.loads(saved_model)

#using the loaded model to make predictions
ynew=loaded_model.predict(X_validation)

# show the inputs and predicted outputs
for i in range(len(X_validation)):
	print("X=%s ,Actual class=%s, Predicted=%s" % (X_validation[i],Y_validation[i], ynew[i]))
