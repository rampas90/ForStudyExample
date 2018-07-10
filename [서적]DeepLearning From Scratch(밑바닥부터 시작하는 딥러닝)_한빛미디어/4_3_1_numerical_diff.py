import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f,x):
    h=10e-50
    return (f(x+h)-f(x))/h

def numerical_diff_mid(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)

print(np.float32(1e-50))

def function_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0.0,20.0,0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

print(numerical_diff_mid(function_1,5))
print(numerical_diff_mid(function_1,10))

def function_2(x):
    return x[0]**2 + x[1]**2

# x0=3, x1=4일때 x0에 대한 편미분을 구해라
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0
print(numerical_diff_mid(function_tmp1,3.0))

# x0=3, x1=4일때, x1에 대한 편미분을 구하라

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

print(numerical_diff_mid(function_tmp2,4.0))