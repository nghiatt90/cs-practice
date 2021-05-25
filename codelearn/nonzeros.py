# https://codelearn.io/training/detail/9587
def nonZeros(v, a):
    s = v + a
    vv = int(str(v).replace('0', ''))
    aa = int(str(a).replace('0', ''))
    ss = int(str(s).replace('0', ''))
    return 'YES' if vv + aa == ss else 'NO'
