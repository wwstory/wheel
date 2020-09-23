import numpy as np

def cal_w(x, y, lv):
    '''
        计算W
    '''
    X = [x**i for i in range(lv)]
    X = np.stack(X, axis=1)
    Y = y.reshape(-1, 1)

    W = least_square(X, Y)
    return W

def least_square(X, Y):
    '''
           XA = Y
        -> X'XA = X'Y
        -> (X'X方阵, 可逆)
        -> A = (X'X)^(-1) X'Y
    '''
    W = np.linalg.inv(X.T @ X) @ X.T @ Y

    return W

def fit(X, W):
    '''
        输出
    '''
    lv = W.shape[0]
    X = [X**i for i in range(lv)]
    X = np.stack(X, axis=1)
    return X @ W

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = np.arange(-1, 1, 0.02)
    y = ((x*x-1)**3+1)*(np.cos(x*2)+0.6*np.sin(x*1.3))

    y1 = y+(np.random.rand(len(x))-0.5)

    w = cal_w(x, y1, 7)
    yw = fit(x, w)
    yw.shape = (yw.shape[0],)

    plt.plot(x, y, color='g', linestyle='-', marker='', label='理想曲线')
    plt.plot(x, y1, color='b', linestyle='', marker='o', label='已知数据点')
    plt.plot(x, yw, color='r', linestyle='', marker='.', label='拟合曲线')
    plt.legend(loc='upper left')
    plt.show()
