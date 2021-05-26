# https://app.codesignal.com/challenge/hqLbYHvpTMZYYLA6h
from collections import Counter as C

couldBeAnagram = lambda a, b: len(a) == len(b) and all(C(a)[i] <= C(b)[i] for i in C(a) if i != '?')
    
