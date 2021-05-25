# https://codelearn.io/training/detail/50599
def star(n):
    r = (n-1) * 4 + 1
    c = (n + n - 1)*2 + n-1 + n-2
    
    rows = ['*']
    spaces = 1
    for i in range(n-2):
        rows.append('*' + (' '*spaces) + '*')
        spaces += 2
    
    half = ' '.join(['*'] * n)
    rows.append(half + (' '*len(rows[-1])) + half)
    
    for i in range(n-1):
        rows.append('*' + (' '*(len(rows[-1])-4)) + '*')
        
    last = list(rows[-1])
    last[len(last)//2] = '*'
    rows[-1] = ''.join(last)
    
    rows += rows[-2::-1]
    
    for i in range(len(rows)):
        rows[i] = rows[i].center(c)
    return rows
