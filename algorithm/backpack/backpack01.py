def backpack01(w, v, c):
    n = len(w)
    dp = [0 for _ in range(c+1)]
    for i in range(n):
        for j in range(c, -1, -1):
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j-w[i]] + v[i])
        # print(dp)
    return dp

if __name__ == "__main__":
    w = [2, 1, 3, 2]
    v = [12, 10, 20, 15]
    c = 5
    # w = [45, 52, 47]
    # v = [45, 52, 47]
    # c = 100
    print(backpack01(w, v, c))