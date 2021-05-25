# https://codelearn.io/training/detail/40929
from collections import Counter

def charWeight(s):
    cnt = Counter(s.lower())
    a = sorted(cnt.most_common(), key=lambda t: t[1]*1000 - ord(t[0]), reverse=True)
    return ''.join('%s{%d}' % t for t in a)
