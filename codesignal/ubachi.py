# https://app.codesignal.com/challenge/WbDRnJGc7TYLdtkcp
def Ubachi(m, k):
    l = len(k)
    kk = sorted(k)
    def trans(s):
        tempk = k[:]
        r = ['' for _ in range(len(s))]
        for i in range(len(s)):
            j = tempk.index(kk[i])
            r[j] = s[i]
            tempk = tempk[:j] + '*' + tempk[j+1:]
            #print(tempk)
        return r
    for _ in range(2):
        mm = [m[i::len(m)//l] for i in range(len(m)//l)]
        #print(mm)
        mmm = list(map(trans, mm))
        m = functools.reduce(lambda x, y: x + ''.join(y), mmm, '')
    return m
