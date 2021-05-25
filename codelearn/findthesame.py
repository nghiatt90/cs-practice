# https://codelearn.io/training/detail/35339
from collections import Counter

def findTheSame(s):
    cnt = Counter(s)
    for c in s:
        if cnt[c] > 1:
            return c*cnt[c]
    return ''
