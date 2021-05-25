# https://codelearn.io/training/detail/22118
def primeString(s):
    for i in range(1, len(s)//2+1):
        sub = s[:i]
        t = ''
        while len(t) < len(s):
            t += sub
        if t[:len(s)] == s:
            return False
    return True
