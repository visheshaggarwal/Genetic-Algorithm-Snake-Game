import numpy as np

n_x = 7 #4 7
n_h = 9 #6 9
n_y = 3
W1_shape = (9,7)
W2_shape = (3,9)

def get_weights_from_encoded(individual):
    W1 = individual[0:W1_shape[0] * W1_shape[1]]
    W2 = individual[W1_shape[0] * W1_shape[1]:]

    return (W1.reshape(W1_shape[0], W1_shape[1]), W2.reshape(W2_shape[0], W2_shape[1]))


def softmax(z):
    s = np.exp(z.T) / np.sum(np.exp(z.T)).reshape(-1, 1)

    return s


def sigmoid(z):
    s = 1 / (1 + np.exp(-z))

    return s


def forward_propagation(X, W1, W2):
    # W1, W2, W3 = get_weights_from_encoded(individual)

    Z1 = np.matmul(W1, X.T)
    # print(Z1)
    A1 = np.tanh(Z1)
    # print(A1)
    Z2 = np.matmul(W2, A1)
    # print(Z2)
    A2 = softmax(np.array(Z2))
    return A2