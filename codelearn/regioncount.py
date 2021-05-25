# https://codelearn.io/training/detail/29367
def regionCount(s):
    d = {'A':2, 'B':3, 'D':2, 'O':2, 'P':2, 'Q':2, 'R':2}
    return sum(d.get(c, 1) for c in s)
