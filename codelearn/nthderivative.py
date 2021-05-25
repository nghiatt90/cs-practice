# https://codelearn.io/training/detail/45183
def nthDerivative(coefficients, n, x):
    while n:
        n -= 1
        for i in range(len(coefficients)):
            coefficients[i] *= i
        if coefficients:
            coefficients.pop(0)
        else:
            return 0
    ans = 0
    for i, c in enumerate(coefficients):
        ans += c * x**i
        ans %= int(1e9 + 7)
    return ans
