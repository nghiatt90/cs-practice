# https://codelearn.io/training/detail/266583
def maxSm(m):
    r, c = len(m), len(m[0])
    dp = [[0]*c for _ in range(r)]
    dp[0] = m[0]
    max_ = 0
    if 1 in dp[0]:
        max_ = 1
    for i in range(r):
        dp[i][0] = m[i][0]
        max_ = max(max_, dp[i][0])

    for i in range(1, r):
        for j in range(1, c):
            if m[i][j] == 0:
                dp[i][j] = 0
                continue
            k = min(dp[i-1][j], dp[i][j-1])
            dp[i][j] = k + m[i-k][j-k]
            max_ = max(max_, dp[i][j])

    return max_ ** 2

