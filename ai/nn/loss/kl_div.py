import numpy as np

def kl_div(input, target):
    '''
        kl散度可以计算2事件的差别
        P_A = P_B 则事件分布完全相同, kl散度等于0
        kl散度计算2个分布不是对称的

        KL散度 = 交叉熵 - 熵 （根据下面的式子直接可得，若熵为常熟，则KL散度等价于交叉熵）

        KL散度： $ D_{KL} (A | B) = \sum_i P_A (x_i) log(\frac{P_A (x_i)}{P_B (x_i)}) = \sum_i P_A (x_i) log(P_A (x_i)) - P_A (x_i) log (P_B(x_i)) $
        熵： $ S(A) = - \sum_i P_A (x_i) log (P_A (x_i)) $
        交叉熵： $ H(A, B) = - \sum_i P_A (x_i) log (P_B(x_i)) $

        一种信息论的解释是：
            熵的意义：是对A事件中的随机变量进行编码所需的最小字节数。
            KL散度的意义：是"额外所需的编码长度"如果我们用B的编码来表示A。
            交叉熵的意义：是当你用B作为密码本来表示A时所需要的"平均的编码长度"。

        交叉熵可以用于计算"学习模型的分布”与"训练数据分布”之间的不同。
        因为训练数据的分布A是给定的，当交叉熵最低时(等于训练数据分布的熵)，我们学到了"最好的模型”。

        ref: https://www.zhihu.com/question/65288314
    '''
    a, b = target, input
    a = a if isinstance(a, np.ndarray) else np.array(a)
    b = b if isinstance(b, np.ndarray) else np.array(b)
    
    a = a.clip(0.001, 1)    # 避免除0和log(0)的错误
    b = b.clip(0.001, 1)    # 避免除0和log(0)的错误

    kl = a * np.log(a/b)
    return np.sum(kl)


if __name__ == "__main__":
    y = [1, 0, 1, 0, 0, 1]
    p = [.7, .1, .8, .3, .2, .7]

    print(kl_div(p, y))