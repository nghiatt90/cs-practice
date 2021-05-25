# https://codelearn.io/training/detail/33084
from collections import Counter
def getDuplicates(a):
    c = Counter(a)
    return [x for x in c if c[x] > 1]
