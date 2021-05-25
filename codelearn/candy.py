# https://codelearn.io/training/detail/7435
def candy(n, a):
    d = 0
    a = set(a)
    max_ = 0
    for i in range(1, n+1):
        cnt = 0
        pos = 0
        while pos <= n:
            pos += i
            if pos in a:
                break
            cnt += 1
        else:
            if cnt > max_:
                max_ = cnt
                d = i
    return d
