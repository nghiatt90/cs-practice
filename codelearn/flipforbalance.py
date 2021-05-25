# https://codelearn.io/training/detail/46471
def flipForBalance(s):
    ans = 0
    d = 0
    for c in s:
        if c == '(':
            d += 1
        else:
            d -= 1
            if d < 0:
                ans += 1
                d = 1
    return ans + d // 2
