import numpy as np
from  DeeplearningFromScratch.function import softmax, cross_entropy_error

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx


class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx

class SoftMaxWithLoss:
    def __init__(self):
        self.loss =None
        self.y = None
        self.t =None

    def forward(self, x,t):
        self.t = t
        self. y = softmax(x)
        self.loss = cross_entropy_error(self.y , self.t)
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx

# x = np.array([[1.0, -0.5], [-2.0, 3.0]])
# print(x)
#
# mask = (x <= 0)
# print(mask)
# out = x.copy()
# print(out)
# out[mask] = 0
# print(out)


# X_dot_W = np.array([[0,0,0],[10,10,10]])
# B = np.array([1,2,3])
#
# print(X_dot_W)
# print(X_dot_W+B)
#
# dY = np.array([[1,2,3],[4,5,6]])
# print(dY)
#
# dB = np.sum(dY, axis=0)
# print(dB)
