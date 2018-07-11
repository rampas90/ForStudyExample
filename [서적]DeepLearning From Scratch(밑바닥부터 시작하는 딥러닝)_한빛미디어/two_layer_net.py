import sys, os

sys.path.append(os.pardir)
from DeeplearningFromScratch.function import *
from DeeplearningFromScratch.gradient import numerical_gradient
from collections import OrderedDict
from DeeplearningFromScratch.layers import *

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

#계층 생성 /5장
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers["Relu1"]=Relu()
        self.layers['Affine2']=Affine(self.params['W2'], self.params['b2'])
        self.lastLayer  = SoftMaxWithLoss()

    # 5장 Predict
    def predict(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x
    # 4장
    # def predict(self, x):
    #     W1, W2 = self.params['W1'], self.params['W2']
    #
    #     b1, b2 = self.params['b1'], self.params['b2']
    #
    #     a1 = np.dot(x, W1) + b1
    #     z1 = sigmoid(a1)
    #     a2 = np.dot(z1, W2) + b2
    #     y = softmax(a2)
    #
    #     return y

    def loss(self, x, t):
        y = self.predict(x)
        # 5장
        return self.lastLayer.forward(y,t)
        # 4장
        # return cross_entropy_error(y, t)


    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        # 5장
        if t.ndim != 1 : t = np.argmax(t,axis=1)
        # 4장
        # t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads

    # 5장
    def gradient(self, x, t):
        self.loss(x,t)

        dout = 1
        dout = self.lastLayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()

        for layer in layers:
            dout = layer.backward(dout)

        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1']= self.layers['Affine1'].db
        grads['W2']=self.layers['Affine2'].dW
        grads['b2']=self.layers['Affine2'].db

        return grads