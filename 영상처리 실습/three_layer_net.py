import numpy as np
from functions import sigmoid, softmax


class ThreeLayerNet:

    def __init__(self, input_size, hidden_size_1, hidden_size_2, output_size, weight_init_std=0.03):
        # 초기 값 지정
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size_1)
        self.params['b1'] = np.zeros(hidden_size_1)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size_1, hidden_size_2)
        self.params['b2'] = np.zeros(hidden_size_2)
        self.params['W3'] = weight_init_std * np.random.randn(hidden_size_2, output_size)
        self.params['b3'] = np.zeros(output_size)

    def predict(self, x):
        # print("func predict start")

        W1, W2, W3 = self.params['W1'], self.params['W2'], self.params['W3']
        b1, b2, b3 = self.params['b1'], self.params['b2'], self.params['b3']
        # 순정파 과정

        # x는 입력층

        # level-1
        # a1 = x dot W1 + b1
        a1 = np.dot(x, W1) + b1
        # z1 =  활성화함수 (a1)
        z1 = sigmoid(a1)

        # level-2
        # a2 = z1 dot W2 + b2
        a2 = np.dot(z1, W2) + b2
        # z2 = 활성화함수 (a2)
        z2 = sigmoid(a2)

        # 출력층
        # a3 = z2 dot W3 + b3
        a3 = np.dot(z2, W3) + b3
        # y = 소프트맥스 함수 (a3)
        y = softmax(a3)

        # print("func predict end")
        return y

    def accuracy(self, x, t):
        # print("func accuracy start")

        # 정확도 계산

        # y는 x의 예측 결과값
        y = self.predict(x)
        y = np.argmax(y, axis=1)  # 훈련 데이터
        t = np.argmax(t, axis=1)  # 실험 데이터

        # 정확도 계산
        accuracy = np.sum(y == t) / float(x.shape[0])

        # print("func accuracy end")
        return accuracy

    def gradient(self, x, t):
        # print("func gradient start")
        W1, W2, W3 = self.params['W1'], self.params['W2'], self.params['W3']
        b1, b2, b3 = self.params['b1'], self.params['b2'], self.params['b3']
        grads = {}

        ##순정파 파트#
        # a1 = x dot W1 + b1
        a1 = np.dot(x, W1) + b1
        # 활성화 함수
        z1 = sigmoid(a1)
        # a2 = z1 dot W2 + b2
        a2 = np.dot(z1, W2) + b2
        # 활성화 함수
        z2 = sigmoid(a2)
        # a3 = z2 dot W3 + b3
        a3 = np.dot(z2, W3) + b3
        # 소프트맥스 함수
        y = softmax(a3)

        ##역전파 파트###

        dLda3 = (y - t)

        grads['W3'] = np.dot(z2.T, dLda3)
        grads['b3'] = dLda3[0]

        dLdz2 = np.dot(dLda3, W3.T)
        dLda2 = z2 * (1 - z2) * dLdz2

        grads['W2'] = np.dot(z1.T, dLda2)
        grads['b2'] = dLda2[0]

        dLdz1 = np.dot(dLda2, W2.T)
        dLda1 = z1 * (1 - z1) * dLdz1

        grads['W1'] = np.dot(x.T, dLda1)
        grads['b1'] = dLda1[0]

        # print("func gradient end")
        return grads
