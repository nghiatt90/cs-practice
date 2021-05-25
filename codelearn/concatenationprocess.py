# https://codelearn.io/training/detail/7664
def concatenationProcess(a):
    while len(a) > 1:
        idx = 0
        l = len(a[0])
        for i, s in enumerate(a):
            if len(s) < l:
                l = len(s)
                idx = i
        x = a.pop(idx)
        # print(x)
        idx = -1
        l = len(a[-1])
        for i in range(-1, -len(a)-1, -1):
            if len(a[i]) < l:
                l = len(a[i])
                idx = i
        y = a.pop(idx)
        # print(y)
        a.append(x+y)
    return a[0]
