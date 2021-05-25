# https://codelearn.io/training/detail/34415
from collections import Counter

def passwordPolicy(password):
    prefix = [Counter()]
    for c in password:
        cnt = Counter(prefix[-1])
        if c.isnumeric():
            cnt[0] += 1
        elif c.islower():
            cnt[1] += 1
        elif c.isupper():
            cnt[2] += 1
        prefix.append(cnt)
    
    for l in range(6, len(password)+1):
        for i in range(len(password)-l+1):
            if len(prefix[i+l] - prefix[i]) == 3:
                return password[i:i+l]
    return ''
