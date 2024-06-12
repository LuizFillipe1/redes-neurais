import numpy as np

def sigmoid(soma):
    return (1 /(1 + np.exp(-soma)))

a = sigmoid(-1.5)

