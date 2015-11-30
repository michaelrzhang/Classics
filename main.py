# import neuralnetwork
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from logisticregression import *

# try random intialization
# smaller test cases

""" 
Author: Michael Zhang
This project is intended to help me practice implement neural networks.
It is my first time using numpy. I will be trying to implement various
machine learning algorithms to determine the authors of literary works.
"""

import numpy as np
import neuralnetwork

authors = ['aristotle', 'dickens', 'doyle', 'emerson', 'hawthorne', 'irving', 
    'jefferson', 'kant', 'keats', 'milton', 'plato', 'poe', 
    'shakespeare', 'stevenson', 'twain', 'wilde']

def get_author_data(name, fraction = 1):
    """ 
    Returns a list with FRACTION of works by NAME.
    Fraction: how much of the data to get
    """
    with open("parsedata/" + name + ".txt") as f:
        content = f.readlines()    
    content = [x.strip('\n') for x in content]
    data = []
    for line in content:
        data.append(list(map(float, line.split())))
    endindex = int(round(len(data) * fraction))
    return data[0: endindex]

# def standardize(m):
#     columns = np.shape(m)[1]
#     for i in range(columns):
#         x = m[:,i]
#         x = preprocessing.scale(x)
#         m[:, i] = x
#     return m

def get_all_author_data(fraction = 1):
    """
    Grabs FRACTION data from all available authors
    Aristotle is hardcoded in in this case.
    """
    i = 0
    data =  np.asarray(get_author_data('aristotle', fraction))
    x = data
    y = np.ones((np.size(data, 0), 1)) * i
    i = i + 1
    for author in authors[1:]:
        data = np.asarray(get_author_data(author, fraction))
        x = np.append(x, data, 0)
        y = np.append(y, np.ones((np.size(data, 0), 1)) * i, 0)
        i = i + 1
    return [x, y]

def validate(predictions, actual):
    compare = np.equal(predictions, actual)
    return np.sum(compare) / compare.size

#Preprocessing
data, result = get_all_author_data(0.8)
training_data_scaler = preprocessing.StandardScaler().fit(data)
data_full, result_full = get_all_author_data(1)
data = training_data_scaler.transform(data)
data_full = training_data_scaler.transform(data_full)

clf = svm.SVC()
clf.fit(data, np.ravel(result))
svm_predictions = np.array([[clf.predict(data[i].reshape(1, -1))[0]] for i in range(np.size(result))])
print("svm result: " + str(validate(svm_predictions, result)))
svm_predictions = np.array([[clf.predict(data_full[i].reshape(1, -1))[0]] for i in range(np.size(result_full))])
print("svm result full: " + str(validate(svm_predictions, result_full)))

clf2 = svm.SVC(C = 1000)
clf2.fit(data, np.ravel(result))
svm_predictions = np.array([[clf2.predict(data[i].reshape(1, -1))[0]] for i in range(np.size(result))])
print("svm2 result: " + str(validate(svm_predictions, result)))
svm_predictions = np.array([[clf2.predict(data_full[i].reshape(1, -1))[0]] for i in range(np.size(result_full))])
print("svm2 result full: " + str(validate(svm_predictions, result_full)))

# Using one-v-all logistic regression
# np.insert(data, 0, 1, axis = 1)
# author = 0
# all_theta = logistic_regression(data, result, author)
# for author in range(1, 16):
#     print(author)
#     theta_temp = logistic_regression(data, result, author)
#     all_theta = np.concatenate((all_theta, theta_temp), 1)

# model_values = np.dot(data, all_theta)
# predictions = np.argmax(model_values, 1)


