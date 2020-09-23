import numpy as np

def bayes_prob(a:np.ndarray, b:np.ndarray) -> np.ndarray:
    """贝叶斯公式

    Args:
        a (np.ndarray): 各自发生事件的概率
        b (np.ndarray): 占比

    Returns:
        np.ndarray: 事件发生来自于谁的概率

    Formula:
        全概率: P(A) = P(A|B1) + P(A|B2) + P(A|B3) + ... + P(A|Bi)
        贝叶斯公式: P(Bi|A) = [P(A|Bi)] / P(A)
    """
    a = a if isinstance(a, np.ndarray) else np.array(a)
    b = b if isinstance(b, np.ndarray) else np.array(b)

    f_p = np.sum(a * b)
    return a*b / f_p


if __name__ == "__main__":
    a = [.02, .01, .03]
    b = [.15, .8, .05]

    print(bayes_prob(a, b))