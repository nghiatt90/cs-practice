# https://codelearn.io/training/detail/24481
from collections import Counter

def wordSquare(letters):
    l = len(letters)
    s = int(l**.5)
    if s*s != l:
        return False
    
    c = Counter(letters)
    odd = 0
    for k, v in c.items():
        if v % 2 == 1:
            odd += 1
    return odd <= s
