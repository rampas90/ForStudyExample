import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from two_layer_net import TwoLayerNet
from three_layer_net import ThreeLayerNet

#데이터 읽기
(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True,flatten=True,one_hot_label=True)

print("x_train.shape: ",x_train.shape)
print("x_train.shape: ",t_train.shape)
print("x_texs.shape: ",x_test.shape)
print("t_test.shape: ",t_test.shape)

network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

train_size=x_train.shape[0]
num_of_epochs = 30
learning_rate = 0.3

train_acc_list = [0.1]
test_acc_list = [0.1]

for epoch_num in range(1,num_of_epochs+1):
    for data_num in range(train_size):
        grad = network.gradient(x_train[[data_num]], t_train[[data_num]])

        for key in ('W1','b1','W2','b2'):
            network.params[key]-=learning_rate *grad[key]

        train_acc = network.accuracy(x_train,t_train)
        test_acc = network.accuracy(x_test,t_test)

        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)

        print("epoch_num=",epoch_num,
              ", data_num=",data_num,
              ", train_acc=",train_acc,
              ", test_acc=",test_acc)

x= np.arange(len(train_acc_list))

plt.plot(x, train_acc_list, label='train acc')
plt.plot(x,test_acc_list,label='test acc',linestyle='--')

plt.xlabel("epochs")
plt.ylabel("accuracy")

plt.ylim(0,1.0)
plt.legend(loc='lower right')
plt.show()
