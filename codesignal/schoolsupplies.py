# https://app.codesignal.com/challenge/rjNJ2CEF6wiXzXawb
S, P = eval(dir()[0])
l = []
r = 0
for s in S:
    d = s.find(' ')
    b = s[d+1:len(s) - (s[-1] == 's')]
    if b not in l:
        l.append(b)
    r += P[l.index(b)] * int(s[:d])
return r
    
    

