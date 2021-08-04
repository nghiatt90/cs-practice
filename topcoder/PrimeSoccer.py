# https://community.topcoder.com/stat?c=problem_statement&pm=10033
# Python2

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

class PrimeSoccer:
    def getProbability(self, pa, pb):
        calc = lambda p, x: p**x * (1-p)**(18-x) * ncr(18, x)
    	primes = [2, 3, 5, 7, 11, 13, 17]
        pa = float(pa)/100
        pb = float(pb)/100
        a = [calc(pa, x) for x in primes]
        b = [calc(pb, x) for x in primes]
        s = 0
        for x in a:
            for y in b:
                s -= x*y
        return s+sum(a)+sum(b)
