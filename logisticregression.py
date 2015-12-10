import numpy as np
from sklearn import preprocessing

#should try using gradient descent algorithm

def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1-sigmoid(z)) 

class LogisticRegression:

    def __init__(self, categories = 2):
        self.categories = categories

    def one_vs_all(self, data, result, num, learning_rate = 0.0000000001):
        """
        Uses random initialization of weights to run logistic regression
        NUM is the group that is labeled 1
        """
        target = np.ones((np.size(result,0), 1)) * num == result
        target = np.array(target, dtype=np.float128)
        theta = np.random.randn(np.shape(data)[1], 1) / 10
        # print("Debugging")
        # print(theta)
        # print(np.shape(theta))
        # print(data)
        # print(np.shape(data))
        # print(result)
        # print(np.shape(result))
        # print(target)
        # print(np.shape(target))

        return self.compute_grad(theta, data, target, learning_rate)

    def fit(self, samples, output):
        """
        Runs one-vs-all logistic regression classification with random initialization of weights
        Returns a matrix that acts as a predictor for every element
        Best results when categories are integers
        """
        samples = np.array(samples)
        output = np.array(output)
        vector_output = output.reshape(np.size(output), 1)
        np.insert(samples, 0, 1, axis = 1)
        all_theta = [self.one_vs_all(samples, vector_output, curr) for curr in set(output)]
        self.predictor = all_theta
        return all_theta

    def compute_grad(self, theta, data, target, learning_rate = 0.002, iterations = 200000):
        """
        Runs the gradient descent algorithm to determine the best theta
        """
        for i in range(iterations):
        # while True:
            predictions = sigmoid(np.dot(data, theta)) 
            difference = predictions - target
            theta = theta - np.dot(np.transpose(data), difference) * learning_rate / np.size(theta, 0)
            # Useful for debugging
            # print("theta")
            # print(theta)
            # print("predictions")
            # print(predictions)
            # print("target")
            # print(target)
            cost = self.costfunc(predictions, target)
            # print("cost")
            print(cost)
            if cost < 10:
                break
        print("predictions")
        print(predictions)
        print("target")
        print(target)
        return theta

    def costfunc(self, predictions, target):
        """
        Logistic regression cost function
        Useful for debugging
        """
        return (np.dot(np.transpose(np.log(predictions)), target) + np.dot(np.transpose(np.log(1 - predictions)), (1 - target))) * -1


# Generate some test data to see how good logistic regression is
logistic_classifier = LogisticRegression()
data = [(np.random.rand() + 10, np.random.rand() + 50) for i in range(10)]
data += [(np.random.rand(), np.random.rand() + 200) for i in range(10)]
# data += [(np.random.rand() - 10 , np.random.rand() + 500) for i in range(10)]
classified = [0 for i in range(10)]
classified += [1 for i in range(10)]
# classified += [2 for i in range(10)]
logistic_classifier.fit(data, classified)

    
