import numpy as np

def softmax(x):
    '''
        $$
            S_i = \frac{e^{V_i}}{\sum_j{e^{V_j}}}
        $$

        作用: 多分类, 计算与标注样本的差距 (归一化概率: 每个类别的分值和为1)
            使用交叉熵作为损失函数时, 计算上非常方便, 损失偏导, 化简后式子简单

            交叉熵损失函数: $Loss = - \sum_i y_i ln a_i$
            偏导: $ \frac{\partial{L_i}}{\partial{f_{y_i}}} = \frac{\partial{(-ln(\frac{e^{f_{y_j}}}{\sum_j^{e^{V_j}}}))}}{\partial{f_{y_i}}} = P_{f_{y_i}} - 1 $
            其中$f_{y_i}$是正样本对于的输出值, 其偏导值则为正样本的值-1即可.
    '''
    xe = np.exp(x)
    z = xe / np.sum(xe)
    return z

if __name__ == "__main__":
    x = np.array([0.1, 0.5, 0.7, 1.2])
    y = softmax(x)
    print(y)