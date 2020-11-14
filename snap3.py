"""
For this question, what we want to do implement is a training algorithm for the linear regression model.

For simplicity, we can assume the number of features in the training set is 2

i.e. we want to learn the parameters for y = w_1 * x_1 + w_2 * x_2 + b.

Normally I would encourage candidates to use gradient descent.

Basically here the goal is, we want to try to "kind of" implement the algorithm from scratch.
"""

import numpy as np

train = []
for _ in range(100):
    x_1 = np.random.random()
    x_2 = np.random.random()
    y = 2 * x_1 + 3 * x_2 + 4 + np.random.normal(0, 0.1)
    train.append([x_1, x_2, y])

# Loss Function: Mean Squared Error
# Let's use the matrix derivative form for y = np.dot(w.T, x)

# define the loss, MSE. n = number of data
def loss(n, y, z):
    L =1/n * np.sum(np.square(y - z))
    return L
# take in the loss, take in the parameter, and take the gradient and update.

def gradient_descent(grad, learn_rate, train):
    # Here are you getting the gradient on the full dataset?
    # I mean, either way is fine, you can either do stochastic gradient descent or just regular gradient descent on the full dataset.
    # But either way, how do you pass in y, z, x_1 and x_2?
    for i in range(100):
        n = len(train)
        z = grad[0]*train[i][0] + grad[1] * train[i][1] + grad[2]
        grad[0] = grad[0] - learn_rate * 2/n * (train[i][2]- z) * train[i][0]
        grad[1] = grad[1] - learn_rate * 2/n * (train[i][2]- z) * train[i][1]
        grad[2] = grad[2] - learn_rate * 2/n * (train[i][2]- z)
    #print(grad)
    return grad

grad = np.ones((3,))
for epoch in range(100):
    grad = gradient_descent(grad, 0.01, train)
    print(grad)
    
#gradient_descent(2,2,2)

