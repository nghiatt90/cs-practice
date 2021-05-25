# https://codelearn.io/training/detail/3868
from collections import Counter

def removeDuplicateCharacters(s):
    res = []
    cnt = Counter(s)
    for c in s:
        if cnt[c] < 2:
            res.append(c)
    return ''.join(res)
