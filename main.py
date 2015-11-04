# import neuralnetwork
import numpy as np
import numpy.matlib
# Aristotle 1
# Emerson 2
# Shakspeare 3
# 
# Text classification
# possibly extend to tweets? more literature?

import numpy as np
import neuralnetwork
 # def __init__(self, hidden_layers, size_of_hidden_layer, data, num_data, output, num_output):
 #        """Initializes random layers and biases for every layer
 #        Layers go firstlayer, hiddenlayers, lastlayer
 #        """
 #        self.layers = layers
 #        self.first_layer = np.asmatrix(np.random(size_of_hidden_layer, num_data))
 #        self.last_layer = np.asmatrix(np.random(num_output, size_of_hidden_layer))
 #        self.hidden_layers = [np.asmatrix(np.random(
 #                    num_output, size_of_hidden_layer)) for i in range(hiddenlayers - 1)]
 #        self.biases = [np.asmatrix(np.random(
 #                    size_of_hidden_layer, 1)) for i in range(hiddenlayers)]
 #        self.last_bias = np.asmatrix(np.random(output, 1))

def get_author_data(name, num):
    """ Returns a list with num elements. Each element represents
    data from a particular author.
    """
    data = []
    for i in range(1, num + 1):
        fname = name + "/" + str(i) + ".txt"
        lines = [line.rstrip('\n') for line in open(fname)]
        data.append(lines)
    return data

# write function for testing, specifying authors later
aristotle = get_author_data("aristotle", 10)
emerson = get_author_data("emerson", 10)
shakespeare = get_author_data("shakespeare", 10)
# sets up 30 training examples
x = np.zeros(shape=(30,4), dtype = np.float64)
x[0:10] = aristotle
x[10:20] = emerson
x[20:30] = shakespeare
y = np.zeros(shape=(30,1))
y[10:20] = 1
y[20:30] = 2

def validate(predictions, actual):
    compare = np.equal(predictions, actual)
    return np.sum(compare) / compare.size

def least_squares_naive(x, y):
    """ Naively attempts to model data with least squares
    x must be full rank and skinny for least squares to work
    """
    coeff = np.linalg.lstsq(x,y)[0]
    raw_predictions = np.asmatrix(x) * np.asmatrix(coeff)
    return numpy.round(raw_predictions)

