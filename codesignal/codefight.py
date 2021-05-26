# https://app.codesignal.com/challenge/okok2rHiWhetqWZfR
def CodeFight(n):
    a = []
    for i in range(1, n+1):
        s = ''
        if i%5 == 0:
            s += 'Code'
        if i%7 == 0:
            s += 'Fight'
        if not s:
            s = str(i)
        a += [s]
    return a
