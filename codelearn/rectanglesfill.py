# https://codelearn.io/training/detail/35269
from pprint import pprint

def rectanglesFill(n):
    dp = [[0] * 16 for _ in range(n + 1)]
    dp[1][0] = dp[1][3] = dp[1][12] = dp[1][9] = dp[1][15] = 1
    MOD = int(1e9+7)
    for i in range(2, n+1):
        j = i-1
        dp[i][0] = (dp[j][0] + dp[j][3] + dp[j][12] + dp[j][9] + dp[j][15]) % MOD
        dp[i][3] = dp[i][12] = (dp[j][0] + dp[j][12]) % MOD
        dp[i][5] = dp[i][10] = dp[j][10] % MOD
        dp[i][6] = dp[j][9] % MOD
        dp[i][9] = (dp[j][6] + dp[j][0]) % MOD
        dp[i][15] = dp[j][0]
    return dp[n][0]
    
    
