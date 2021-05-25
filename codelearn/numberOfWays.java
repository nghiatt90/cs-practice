// https://codelearn.io/training/detail/128942
int numberOfWays(int n, int a, int b, int c)
{
    int[] cost = new int[] {1, 2, 4};
    int[] m = new int[] {a, b, c};
    int s = n * 2;
    n = 3;
    return smarket(s, n, cost, m);
}


int smarket(int s, int n, int[] c, int[] m)
{
    s += 1;
    n += 1;
    int[][] dp = new int[s][n];
    for (int j = 0; j < n; ++j)
        dp[0][j] = 1;
    for (int i = 1; i < s; ++i)
        for (int j = 1; j < n; ++j) {
            int max_buy = Math.min(m[j-1], i/c[j-1]);
            for (int k = 0; k <= max_buy; ++k) {
                dp[i][j] += dp[i-k*c[j-1]][j-1];
            }
        }
    return dp[s-1][n-1];
}

