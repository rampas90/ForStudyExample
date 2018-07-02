import numpy as np
import pickle
from mnist import load_mnist
from functions import sigmoid , softmax
from PIL import Image


def img_show(img):
    pil_img=Image.fromarray(np.uint8(img))
    pil_img.show()

def get_data():
    (x_train,t_train),(x_test,t_test)=load_mnist(normalize=True,flatten=True,one_hot_label=False)
    return x_test,t_test

def init_network():
    with open("sample_weight.pkl",'rb') as f:
        network=pickle.load(f)
    return network

def predict(network,x):
    W1 = network['W1']
    W2=network['W2']
    W3 = network['W3']

    b1=network['b1']
    b2=network['b2']
    b3=network['b3']

    a1=np.dot(x,W1)+b1
    z1=sigmoid(a1)

    a2=np.dot(z1,W2)+b2
    z2=sigmoid(a2)

    a3=np.dot(z2,W3)+b3
    y=softmax(a3)

    return y

x,t=get_data()
print("len(x)=",len(x))

network = init_network()
accuracy_cnt=0

p=np.zeros_like(t,np.uint8)

rr=0
for i in range(len(x)):
    y=predict(network,x[i])
    p[i]=np.argmax(y)

    if p[i]==t[i] :
        accuracy_cnt+=1
    else :
        print("i=",i,"p[i]=",p[i],"t[i]=",t[i])
        img = 255*(x[i].reshape(28,28))
        if rr<10:
            img_show(img)
            rr+=1
print("Accuracy:",float((accuracy_cnt)/len(x)))
