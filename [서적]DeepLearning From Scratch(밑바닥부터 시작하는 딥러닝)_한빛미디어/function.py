import numpy as np

def step_function(x):
    y = x>0
    return y.astype(np.int)

def sigmoid(x):
    return 1 / (1+np.exp(-x))


def relu(x):
    return np.maximum(x,0)



def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x) # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x))


# def softmax(a):
#     c= np.max(a)
#     exp_a = np.exp(a-c) #오버플로 대책
#     sum_exp_a = np.sum(exp_a)
#     y= exp_a/sum_exp_a
#     return y
#


# def cross_entropy_error(y, t):
#     delta = 1e-7
#     if y.ndim==1:
#         t= t.reshape(1,t.size)
#         y=y.reshape(1,y.size)
#     batch_size = y.shape[0]
#     return -np.sum(t*np.log(y+delta))/batch_size


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size



# def cross_entropy_error(y, t):
#     delta = 1e-7
#     return -np.sum(t * np.log(y + delta))

def mean_squared_errpr(y,t):
    return 0.5 * np.sum((y-t)**2)

#
# def numerical_gradient(f,x):
#     h=1e-4
#     grad = np.zeros_like(x);
#
#     for idx in range(x.size):
#         tmp_val = x[idx]
#
#         x[idx]=tmp_val+h
#         fxh1 = f(x)
#
#         x[idx]=tmp_val-h
#         fxh2=f(x)
#
#         grad[idx]=(fxh1-fxh2)/(2*h)
#         x[idx]=tmp_val
#
#     return grad