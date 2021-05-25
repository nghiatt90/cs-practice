# https://codelearn.io/training/detail/34670
def sumOfOddNumbers(a, b):
    MOD = 10000007
    a = (a+1)//2*2 + 1
    b = b//2*2 - 1
    if b < a:
        return 0
    r = (b-a) // 2 + 1
    # print(a, b, r)
    s = (a+b)*(r/2)
    return int(s) % MOD
