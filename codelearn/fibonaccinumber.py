# https://codelearn.io/training/detail/10434
def fibonacciNumber(n):
    f = [0] * max(2, n+1)
    f[1] = 1
    MOD = int(1e9+7)
    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2]) % MOD
    return f[n]
