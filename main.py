import neuralnetwork
import numpy as np
from sklearn import preprocessing
from sklearn import svm

# try random intialization
# smaller test cases

""" 
Author: Michael Zhang
This project is intended to help me practice implement neural networks.
It is my first time using numpy. I will be trying to implement various
machine learning algorithms to determine the authors of literary works.
"""

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

# def one_vs_all(self, data, result, num, learning_rate = 0.0000000001):
#         """
#         Uses random initialization of weights to run logistic regression
#         NUM is the group that is labeled 1
#         """
#         target = np.ones((np.size(result,0), 1)) * num == result
#         target = np.array(target, dtype=np.float128)
#         theta = np.random.randn(np.shape(data)[1], 1) / 10

# need to organize code better
#Preprocessing
data, result = get_all_author_data(0.8)
training_data_scaler = preprocessing.StandardScaler().fit(data)
data_full, result_full = get_all_author_data(1)
data = training_data_scaler.transform(data)
data_full = training_data_scaler.transform(data_full)

"""Default SVC"""
clf = svm.SVC()
clf.fit(data, np.ravel(result))
svm_predictions = np.array([[clf.predict(data[i].reshape(1, -1))[0]] for i in range(np.size(result))])
print("svm result: " + str(validate(svm_predictions, result)))
svm_predictions = np.array([[clf.predict(data_full[i].reshape(1, -1))[0]] for i in range(np.size(result_full))])
print("svm result full: " + str(validate(svm_predictions, result_full)))

"""Adjusted parameter C"""
clf2 = svm.SVC(C = 1000)
clf2.fit(data, np.ravel(result))
svm_predictions = np.array([[clf2.predict(data[i].reshape(1, -1))[0]] for i in range(np.size(result))])
print("svm2 result: " + str(validate(svm_predictions, result)))
svm_predictions = np.array([[clf2.predict(data_full[i].reshape(1, -1))[0]] for i in range(np.size(result_full))])
print("svm2 result full: " + str(validate(svm_predictions, result_full)))

"""Neural network"""
"""
Need to first modify data into usable format
Each piece of data should have an input that is 204x1 and output that is 16x1

The below code is trying to convert output to vectors with 1s in one entry(the correct category) and 0s everywhere else
"""
sizes = [204, 50, 16]
categories = 16
result_matrix = np.zeros([np.shape(result)[0], categories])
for i in range(np.shape(result)[0]):
    result_matrix[i][result[i][0]] = 1
testing = neuralnetwork.NeuralNetwork(sizes)
# Initial predictions
testing.make_predictions(data)
testing.train(data, result_matrix, 5)
# target = []
# for r in result:
#     output = np.zeros([categories, 1])
#     output[r[0]] = 1
#     target += output



# I am having issues with convergence with this model
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


