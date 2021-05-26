# https://app.codesignal.com/challenge/2LAiEGXS9ezxCZ8k3
from collections import deque

def longestWordLadder(s, e, w):
    def A(x, y):
        x.append(y)
    R = range
    L = len
    
    w.sort()
    w = [s] + w + [e]
    n = len(w)
    
    s = 0
    e = n - 1
    g = {i:[] for i in R(n)}
    
    for i in R(n):
        for j in R(i+1, n):
            if sum(w[i][k] != w[j][k] for k in R(L(w[0]))) == 1:
                A(g[i], j)
                A(g[j], i)
    
    S = deque([(0, [])])
    r = []
    while S:
        v, p = S.pop()
        if v not in p:
            if v == e:
                if L(r) < L(p) or L(r) == L(p) and p < r:
                    r = p[:] 
            A(p, v)
            for x in g[v]:
                A(S, (x, p[:]))
    
    return [w[i] for i in r]+[w[e]] if r else []
            
