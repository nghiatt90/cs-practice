# https://codelearn.io/training/detail/9944
def segmentNumber(a, segLen):
    a.sort()
    end = a[0] - 1
    ans = 0
    for x in a:
        if x > end:
            ans += 1
            end = x + segLen
    return ans
