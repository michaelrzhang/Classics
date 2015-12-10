import numpy as np

class NN:
    """Using neural network that forward propagates
    and then improves through back propagation.
    """
    def __init__(self, sizes):
        """Initializes random layers and biases for every layer
        SIZES gives the sizes of the desired layers
        Assumes that len(SIZES) is the number of layers

        As a quick example 
        input sizes 3 5 2
        should initialize random biases of size 5x1 and 2x1
        random weights of size 5x3 and 2x5
        
        For learning purposes:
        -There does not seems to be any meaningful distinction between different layers
        (so between input, hidden, and output)
        -We can treat all the layers as the same.
        -No bias is needed for the first layer (which makes sense, number of weights/biases
            should be same)
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.weights = [np.random.randn(output_size, input_size)
                        for output_size, input_size in zip(sizes[1:], sizes[:-1])]
        self.biases = [np.random.randn(layer_size, 1) for layer_size in sizes[1:]]  

    def feedforward():
        return

    def backpropagte():
        return


def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1-sigmoid(z))