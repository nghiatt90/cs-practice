# https://codelearn.io/training/detail/42171
def findDistinctNumbers(a):
    s = set()
    res = []
    for i in a:
        if i in s:
            continue
        s.add(i)
        res.append(i)
    return res
