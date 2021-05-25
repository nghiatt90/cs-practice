# https://codelearn.io/training/detail/46473
def gemPower(n):
    dp = [[0] * 3 for _ in range(n+1)]
    dp[1][0] = dp[1][1] = dp[1][2] = 1
    MOD = int(1e9+7)
    for i in range(2, n+1):
        dp[i][0] = dp[i][1] = (dp[i-1][2] + dp[i-1][1]) % MOD
        dp[i][2] = sum(dp[i-1]) % MOD
    return sum(dp[n]) % MOD
