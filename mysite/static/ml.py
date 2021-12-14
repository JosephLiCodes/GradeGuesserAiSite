# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import tensorflow
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plot
from matplotlib import style
import pickle
from django.contrib.staticfiles import finders
from django.conf import settings
data = pd.read_csv("student-mat.csv", sep=";")
print(data.head())
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
#print(data.head())
input = pd.read_csv("testdata.csv", sep=",")
input = input[["G1", "G2", "studytime", "failures", "absences"]]
predict = "G3"
print(input)
X = np.array(data.drop([predict],1)) #array with everything except for G3 (we are predicting G3)
Y = np.array(data[predict]) #array with only g3 values
input_array = np.array(input)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1) #10 percent of data is going to be set aside to get tested for accurate results

# TRAIN MODEL MULTIPLE TIMES FOR BEST SCORE
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)
best = linear.score(x_test, y_test)
print("initial: ", best)

for _ in range(20):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    # If the current model has a better score than one we've already trained then save it
    #print(acc)
    if acc > best:
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)

#load model with highest accuracy
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)
print("your predicted score out of 20 is: ", linear.predict(input_array))
acc = linear.score(x_test, y_test) #accuracy of model

print("used model accuracy: ", best)
predictions = linear.predict(x_test)
#for x in range(len(predictions)):
    #print(predictions[x], x_test[x], y_test[x])g

def getResult(f):
    data = pd.read_csv(f)
    data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
    input_array = np.array(input)
    print("your predicted score out of 20 is: ", linear.predict(input_array))