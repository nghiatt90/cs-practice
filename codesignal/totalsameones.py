# https://app.codesignal.com/challenge/dBrLcRdRDSPKeHzd5
f = lambda x: 1 if x < 1 else x * f(x - 1)
c = lambda n, r: 0 if r > n else f(n) / f(r) / f(n-r)
k = lambda x: 1 if x < 2 else k(int(bin(x)[3:], 2)) + c(len(bin(x)) - 3, bin(x).count('1'))
totalSameOnes = k
    
    
