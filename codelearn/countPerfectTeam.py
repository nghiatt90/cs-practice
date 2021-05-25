# https://codelearn.io/training/detail/229602
def countPerfectTeam(a, b, c):
    ret = min([a, b, c])
    if ret == a or ret == b:
        return ret
    a -= ret
    b -= ret
    c -= ret
    ret2 = min(a, b)
    rem = max(a, b) - ret2
    if rem >= ret2:
        return ret + ret2
    return (a+b) // 3 + ret

