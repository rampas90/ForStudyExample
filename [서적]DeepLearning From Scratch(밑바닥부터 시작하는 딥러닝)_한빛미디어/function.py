import numpy as np

def step_function(x):
    y = x>0
    return y.astype(np.int)

def sigmoid(x):
    return 1 / (1+np.exp(-x))


def relu(x):
    return np.maximum(x,0)


def softmax(a):
    c= np.max(a)
    exp_a = np.exp(a-c) #오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y= exp_a/sum_exp_a
    return y
