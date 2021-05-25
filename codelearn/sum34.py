# https://codelearn.io/training/detail/44232
def sum34(n):
    cnt = 2**n
    ans = 0
    while cnt:
        ans += cnt%10
        cnt //= 10
    return ans
