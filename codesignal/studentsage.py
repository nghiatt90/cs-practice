# https://app.codesignal.com/challenge/95w2q3BNpMT5M2yfs
def studentsAge(s):
    g = [0] * 6**7
    c = 0
    for i in s:
        c += g[i - 1]
        g[i] += 1
    return c
