# https://codelearn.io/training/detail/5102
def countSumOfTwoRepresentations(n, l, r):
    cnt = 0
    for i in range(l, r+1):
        if i <= n-i <= r:
            cnt += 1
    return cnt
