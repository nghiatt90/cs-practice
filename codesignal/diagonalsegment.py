# https://app.codesignal.com/challenge/JjgwffgmTu6wy3cfo
(x,y), l = eval(dir()[0])

for i in range(1, l):
    f = l*l - i*i
    k = int(f**.5)
    if k*k == f:
        return x+i, y+k

