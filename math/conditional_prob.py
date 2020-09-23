def conditional_prob(a:float, ab:float) -> float:
    """条件概率

    Args:
        a (float): A概率
        ab (float): AB概率

    Returns:
        float: A发生的条件下，B发生的概率
    
    Formula:
        P(B|A) = P(AB) / p(A)
    """
    return ab/a


if __name__ == "__main__":
    a = 3/4
    # b = 1/4
    ab = 1/4
    print(conditional_prob(a, ab))