import numpy as np

class NN:
    """Using neural network that forward propagates (using one-vs-all)
    and then improves through back propagation.
    """
    def __init__(self, hidden_layers, size_of_hidden_layer, data, num_data, output, num_output):
        """Initializes random layers and biases for every layer
        Layers go firstlayer, hiddenlayers, lastlayer
        """
        self.layers = layers
        self.first_layer = np.asmatrix(np.random(size_of_hidden_layer, num_data))
        self.last_layer = np.asmatrix(np.random(num_output, size_of_hidden_layer))
        self.hidden_layers = [np.asmatrix(np.random(
                    num_output, size_of_hidden_layer)) for i in range(hiddenlayers - 1)]
        self.biases = [np.asmatrix(np.random(
                    size_of_hidden_layer, 1)) for i in range(hiddenlayers)]
        self.last_bias = np.asmatrix(np.random(output, 1))

    def backpropagte():
        return


def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1-sigmoid(z))