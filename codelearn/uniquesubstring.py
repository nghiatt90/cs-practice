# https://codelearn.io/training/detail/9319
from collections import defaultdict
def uniqueSubstring(s):
    for l in range(1, len(s)+1):
        d = defaultdict(lambda: 0)
        for i in range(len(s)-l+1):
            sub = s[i:i+l]
            d[sub] += 1
        a = [k for k, v in d.items() if v == 1]
        if a:
            return sorted(a)[0]
