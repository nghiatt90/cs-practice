# https://codelearn.io/training/detail/32281
def maxXor(a):
    ans = 0
    for mask in range(2**len(a)):
        t = 0
        for i in range(len(a)):
            if mask & (1<<i):
                t ^= a[i]
        ans = max(ans, t)
    return ans

