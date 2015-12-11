import numpy as np
"""
Much of this code is motivated by Andrew Ng's course
and Michael Nielsen's Neural Networks and Deep Learning book

author: Michael Zhang
"""

class NeuralNetwork:
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
        self.weights = [np.random.randn(output_size, input_size) / 2 
                        for output_size, input_size in zip(sizes[1:], sizes[:-1])]
        self.biases = [np.random.randn(layer_size, 1) / 2 for layer_size in sizes[1:]]  

    def make_predictions(self, test_input):
        """
        Given list of input vectors, returns the neural network prediction for each 
        vector.
        """
        return [np.argmax(self.predict(x)) for x in test_input]

    def predict(self, x):
        """Returns output of neural network given x as input"""
        assert x.size == self.sizes[0]
        output = x.reshape(self.sizes[0], 1)
        for w, b in zip(self.weights, self.biases):
            output = sigmoid(np.dot(w, output) + b)
        return output

    def compute_cost(self, x, y):
        cost = 0
        for example, target in zip(x, y):
            prediction = self.predict(example)
            target = target.reshape(target.size, 1)
            cost += np.linalg.norm(prediction - target)
        return cost

    # should play around with parallelizing this code
    def train(self, training_in, training_out, training_amount, rate = 0.5):   
        """
        Runs the backpropation algorithm AMOUNT times with learning RATE
        Also takes in training data and desired results.
        """
        training_set_size = training_out.shape[0]
        for i in range(training_amount):
            # track overall changes from training session
            delta_weights = [np.zeros(weight.shape) for weight in self.weights]
            delta_biases = [np.zeros(bias.shape) for bias in self.biases]
            for x, y in zip(training_in, training_out):
                delta_w, delta_b = self.backpropagate(x, y)
                delta_weights = [a + b for a, b in zip(delta_weights, delta_w)]
                delta_biases = [a + b for a, b in zip(delta_biases, delta_b)]
            self.weights = [w - dw * rate / training_set_size for w, dw in zip(self.weights, delta_weights)]
            self.biases = [b - db * rate / training_set_size for b, db in zip(self.biases, delta_biases)]

    def backpropagate(self, x, y):
        """
        Computes the gradients from a single training example (x, y)
        """
        assert x.size == self.sizes[0]
        assert y.size == self.sizes[-1]
        x = x.reshape(self.sizes[0], 1)
        y = y.reshape(self.sizes[-1], 1)

        weight_derivatives = [np.zeros(weight.shape) for weight in self.weights]
        bias_derivatives = [np.zeros(bias.shape) for bias in self.biases]
        # forward propagation
        activations = [x]
        zs = []
        current = x
        for weight, bias in zip(self.weights, self.biases):
            current = np.dot(weight, current) + bias
            zs.append(current)
            activation = sigmoid(current)
            activations.append(activation)

        error = (activations[-1] - y) * sigmoid_prime(zs[-1])
        # back propagation of error
        # Note to self (and readers): understanding the following code/equations is probably the hardest part
        # It's worthwhile to walk through a smaller example to better understand exactly what happens.
        
        # need to handle last layer separately otherwise -1(1) + 1 = 0, and we can't use negative indiceing
        bias_derivatives[-1] = error
        weight_derivatives[-1] = np.dot(error, activations[-2].transpose())
        propagated_error = error
        # traversing layers in reverse order, while propagating error back
        # follows the equations from Nielsen's book
        for layer in range(2, self.num_layers):
            z = zs[-1 * layer]
            propagated_error = np.dot(self.weights[-1 * layer + 1].transpose(), propagated_error) * sigmoid_prime(z)
            bias_derivatives[-1 * layer] = propagated_error
            weight_derivatives[-1 * layer] = np.dot(propagated_error, activations[-1 * layer - 1].transpose())
        return weight_derivatives, bias_derivatives
       

def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z) * (1-sigmoid(z))