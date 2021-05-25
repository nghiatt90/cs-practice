# https://codelearn.io/training/detail/34654
def keyboardLayout(k1, k2, t):
    k1 += k1.upper()
    k2 += k2.upper()
    d = dict(zip(k1, k2))
    return ''.join(d.get(c, c) for c in t)
