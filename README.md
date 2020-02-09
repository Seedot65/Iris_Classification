# Iris_Classification
This is a M.L project to classify the dataset,consisting of the three classes of flowers,and their description,namely,sepal length in cm,sepal width in cm,petal length in cm,petal width in cm.

The first step was to load the data using pandas,after having saved the original data as a csv file in the local directory.Then upon visualising the data as a scatterplot matrix using seaborn,a sharp disticttion was observed between iris stetosa and the others. 
Then the classification problem was tested using different available algorithms.Stratified 10 fold method was used.That is,the data was divided into 10 folds with each approx same data distribution,training was done on 9 and evaluation on the tenth.SVM was found to have higest accuracy of 98.4615 percent.
Then SVM was used to build the model.
This model was chosen because:
It relies on the making of a hyperplane separating the points,with factors like gamma and regularisation parameter determining the accurracy and time required .
Regularisation parameter is the factor which ensures how much tolerance we can permit,which comes at a cost of time.
Gamma parameter tunes whether far off datapoints from the location of the hyperplane should considered or not.
Finally, the model was evaluated,stored ,loaded(by pickling it),and the actual and prdicted Values of validation dataset was printed.
