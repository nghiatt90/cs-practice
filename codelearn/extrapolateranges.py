# https://codelearn.io/training/detail/44200
def extrapolateRanges(s):
    if any(not c.isnumeric() and c != ',' for c in s):
        return 'undefined'
    n = [int(x) for x in s.split(',')]
    n = sorted(set(n))
    n.append(99999999)
    ans = []
    lpos, lval = 0, n[0]
    for i in range(1, len(n)):
        if n[i] == n[i-1]+1:
            continue
        if i == lpos + 1:
            ans.append(str(lval))
        else:
            ans.append(f'{lval}-{n[i-1]}')
        lpos, lval = i, n[i]
    return ','.join(ans)
