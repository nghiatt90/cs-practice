# https://codelearn.io/training/detail/116691
from collections import Counter
def mode(arr):
    c = Counter(arr)
    _, y = c.most_common(1)[0]
    s = 0
    for k, v in c.items():
        if v == y:
            s += k * v
    return s

