import numpy as np

def full_prob(a:np.ndarray, b:np.ndarray) -> np.ndarray:
    """全概率公式

    Args:
        a (np.ndarray): 各自发生事件的概率
        b (np.ndarray): 占比

    Returns:
        np.ndarray: 事件发生概率
    
    Formula:
        P(A) = P(A|B1) + P(A|B2) + P(A|B3) + ... + P(A|Bi)
    """
    a = a if isinstance(a, np.ndarray) else np.array(a)
    b = b if isinstance(b, np.ndarray) else np.array(b)

    return np.sum(a * b)

if __name__ == "__main__":
    a = [0.02, 0.01, 0.01]
    b = [0.3, 0.5, 0.2]

    print(full_prob(a, b))