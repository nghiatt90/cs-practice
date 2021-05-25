# https://codelearn.io/training/detail/33359
def changumangu23(n):
    dp = [-1] * max(n+1, 5)
    dp[0] = dp[1] = 0
    dp[2] = dp[3] = 1
    MOD = int(1e9) + 7
    for i in range(4, n+1):
        dp[i] = (dp[i-2] + dp[i-3]) % MOD
    return dp[n]
