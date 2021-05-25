# https://codelearn.io/training/detail/131330
def biggestRemainer(arr):
    a = sorted(set(arr))
    if len(a) < 2:
        return 0
    return a[-2]
