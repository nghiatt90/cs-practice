# https://codelearn.io/training/detail/34597
from string import ascii_lowercase as chars

def hackIt(s):
    m = dict(zip(chars, chars[::-1]))
    ans = []
    for c in s:
        k = m.get(c.lower(), c)
        if c.isupper():
            k = k.upper()
        ans.append(k)
    return ''.join(ans)
