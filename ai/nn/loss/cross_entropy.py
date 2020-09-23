import numpy as np

def cross_entropy(input, target):
    '''
        $ L = \frac{1}{N} \sum_i L_i = \frac{1}{N} \sum_i -[y_i log(p_i) + (1-y_i) log(1-p_i)] $
    '''
    y, p = target, input
    y = y if isinstance(y, np.ndarray) else np.array(y)
    p = p if isinstance(p, np.ndarray) else np.array(p)
    
    n = len(input)
    return - np.sum(y * np.log(p) + (1 - y) * np.log(1-p)) / n


if __name__ == "__main__":
    y = [1, 0, 1, 0, 0, 1]
    p = [.7, .1, .8, .3, .2, .7]

    print(cross_entropy(p, y))