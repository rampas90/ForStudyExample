import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from three_layer_net import ThreeLayerNet

#데이터 읽기
(x_train,t_train),(x_test,t_test) = load_mnist(normalize=True,flatten=True,one_hot_label=True)

print("x_train.shape: ",x_train.shape)
print("x_train.shape: ",t_train.shape)
print("x_texs.shape: ",x_test.shape)
print("t_test.shape: ",t_test.shape)

network = ThreeLayerNet(input_size=784,hidden_size_1=50,hidden_size_2=30,output_size=10)

train_size=x_train.shape[0]
# 반복 회수 지정 30회 반복
num_of_epochs = 30
# 학습률 지정 = 0.3
learning_rate = 0.3

train_acc_list = [0.1]
test_acc_list = [0.1]

# epoch 수 만큼 반복 (30)
for epoch_num in range(1,num_of_epochs+1):
    # data set 개수 만큼 반복 (600)
    for data_num in range(train_size):
        
        # grad 값 계산
        grad = network.gradient(x_train[[data_num]], t_train[[data_num]])

        # 학습률과 grad값을 통해서 가중치 업데이트
        for key in ('W1','b1','W2','b2','W3','b3'):
            network.params[key]-=learning_rate *grad[key]

        # 정확도 계산
        train_acc = network.accuracy(x_train,t_train)
        test_acc = network.accuracy(x_test,t_test)

        # 결과 저장
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)

        print("epoch_num=",epoch_num,
              ", data_num=",data_num,
              ", train_acc=",train_acc,
              ", test_acc=",test_acc)


#최종 결과를 Graph로 그려준다.
x= np.arange(len(train_acc_list))

plt.plot(x, train_acc_list, label='train acc')
plt.plot(x,test_acc_list,label='test acc',linestyle='--')

plt.xlabel("epochs")
plt.ylabel("accuracy")

plt.ylim(0,1.0)
plt.legend(loc='lower right')
plt.show()
