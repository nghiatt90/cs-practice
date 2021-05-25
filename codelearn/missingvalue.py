# https://codelearn.io/training/detail/40651
from collections import Counter

def missingValue(a):
    counter = Counter(a)
    (y, _), (x, _) = counter.most_common()[-2:]
    return x*x*y
