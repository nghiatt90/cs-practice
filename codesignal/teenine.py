# https://app.codesignal.com/challenge/noThgu6K88YPqceQy
def teeNine(m):
    z = '        abc def ghi jkl mno pqrstuv wxyz'
    
    r = []
    l = 0
    c = 0
    for x in map(lambda x: z.index(x.lower())//4 if x.isalpha() else x, m):
        if isinstance(x, int):
            q = z[x*4:x*4+4].strip()
            if x == l:
                c += 1
                r[-1] = q[c%len(q)]
            else:
                r.append(q[0])
                l = x
                c = 0
        else:
            r.append(x)
            l = 0
            c = 0
            
    return ''.join(r)
    
