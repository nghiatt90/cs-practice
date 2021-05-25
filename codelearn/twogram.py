# https://codelearn.io/training/detail/34650
from collections import Counter

def twoGram(s):
    subs = [s[i]+s[i+1] for i in range(len(s)-1)]
    c = [(-v, k) for k, v in Counter(subs).items()]
    c.sort()
    # return c
    return c[0][1]
