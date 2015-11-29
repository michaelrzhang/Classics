import numpy as np
from sklearn import preprocessing

def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1-sigmoid(z)) 

def standardize(m):
    columns = np.shape(m)[1]
    for i in range(columns):
        x = m[:,i]
        x = preprocessing.scale(x)
        m[:, i] = x
    return m

def logistic_regression(data, result, num, learning_rate = 0.0000000001):
    """
    Uses random initialization of weights to run logistic regression
    NUM is author we are currently classifying
    """
    target = np.ones((np.size(result,0), 1)) * num == result
    target = np.array(target, dtype=np.float128)
    theta = np.random.randn(np.size(data, 1), 1)
    return compute_grad(theta, data, target, learning_rate)

def compute_grad(theta, data, target, learning_rate = 0.0000000001):
    """
    Runs the gradient descent algorithm to determine the best theta
    """
    for i in range(500):
        # print(theta)
        predictions = sigmoid(np.dot(data, theta)) 
        difference = predictions - target
        # cost = costfunc(predictions, target)
        # print(cost)
        theta = theta - np.dot(np.transpose(data), difference) * learning_rate / np.size(theta, 0)
    return theta

def costfunc(predictions, target):
    """
    Logistic regression cost function
    Useful for debugging
    """
    return (np.dot(np.transpose(np.log(predictions)), target) + np.dot(np.transpose(np.log(1 - predictions)), (1 - target))) * -1

