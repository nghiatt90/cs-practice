# https://codelearn.io/training/detail/34509
def leftRigthCipher(s):
    ans = []
    s = list(s)
    i = -1 if len(s)&1 == 0 else 0
    while s:
        ans.append(s.pop(i))
        i = 0 if i else -1
    return ''.join(ans[::-1])

