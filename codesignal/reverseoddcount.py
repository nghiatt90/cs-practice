# https://app.codesignal.com/challenge/NZLcmPoRjWAMfCbx2
s = list(eval(dir()[0])[0])
from collections import Counter as C
c = C(s)
i, j = 0, len(s) - 1
while i < j:
    while c[s[i]] & 1 < 1 and i < j:
        i += 1
    while c[s[j]] & 1 < 1 and i < j:
        j -= 1
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
return ''.join(s)
