import numpy as np

def mse_loss(y, p):
    '''
        mean squared error
    '''
    y = y if isinstance(y, np.ndarray) else np.array(y)
    p = p if isinstance(p, np.ndarray) else np.array(p)

    n = len(p)
    return np.sum((y - p) ** 2) / n

if __name__ == "__main__":
    y = [1, 0, 1, 0, 0, 1]
    p = [.7, .1, .8, .3, .2, .7]
    print(mse_loss(y, p))