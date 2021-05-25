# https://codelearn.io/training/detail/35001
import string
digs = string.digits + string.ascii_letters


def baseChange(x, base):
    """Decimal to custom base"""
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)
