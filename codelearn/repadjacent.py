# https://codelearn.io/training/detail/35085
import re

def repAdjacent(s):
    ls = []
    last = ''
    for c in s:
        if c == last:
            ls[-1] = '*'
        else:
            ls.append(c)
            last = c
    return len(re.findall('\*{2,}', ''.join(ls)))

