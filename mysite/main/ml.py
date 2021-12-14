import os
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
from django.contrib.staticfiles import finders

pickle_in = open(finders.find("studentgrades.pickle"), "rb")
linear = pickle.load(pickle_in)

def getResult(data):
    data = data[["G1", "G2", "studytime", "failures", "absences"]]
    input_array = np.array(data)
    result = linear.predict(input_array)
    print("your predicted score out of 20 is: ", result)
    return result