# https://codelearn.io/training/detail/40949
def findTheFormula(seq):
    x, y, z = seq
    for k in range(-5000, 5001):
        b = y - k*x
        if z == k*y + b:
            break
    dk = '' if k == 1 else '-' if k == -1 else k
    db = '' if b == 0 else f'+{b}' if b > 0 else b
    return f'{dk}n{db}'
