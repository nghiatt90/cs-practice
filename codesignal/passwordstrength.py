# https://app.codesignal.com/challenge/L3M46HoM4yk4dfHLi
def passwordStrength(p):
    s = [0]*4
    R = range(4)
    for c in set(p):
        d = ord(c)
        if 123 > d > 96: s[0] += 1
        elif 91 > d > 64: s[1] += 1
        elif 58 > d > 47: s[2] += 1
        else: s[3] += 1
    g = [.75, .6, .6, .5]
    z = [26, 26, 10, 32]
    r = [1 - g[i]**s[i] for i in R]
    return math.log(sum([(r[i] * z[i]) for i in R]) ** len(p), 2)
    

