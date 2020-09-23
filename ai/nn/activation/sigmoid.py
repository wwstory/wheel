import numpy as np

'''
对数几率函数（Sigmoid）：$y = \sigma (z) = \frac{1}{1+e^{-z}}$

作用：将值限制在 [0, 1]

为什么逻辑回归要使用sigmoid？

'''
def sigmoid(z):
    return 1 / (1 + np.e ** (-z))