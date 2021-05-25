# https://codelearn.io/training/detail/34457
def evenSubStrings(s):
    ans = 0
    for i, c in enumerate(s):
        if int(c) % 2:
            continue
        ans += (i+1)
    return ans

