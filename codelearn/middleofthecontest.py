# https://codelearn.io/training/detail/45314
from datetime import datetime

def middleOfTheContest(s1, s2):
    h1, m1 = [int(x) for x in s1.split(':')]
    h2, m2 = [int(x) for x in s2.split(':')]
    a1 = datetime(2019, 1, 1, h1, m1)
    a2 = datetime(2019, 1, 1, h2, m2)
    delta = a2 - a1
    ret = a1 + delta // 2
    return str(ret)[11:16]
