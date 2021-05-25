# https://codelearn.io/training/detail/188415
def findMissingDigit(expression):
    candidates = set('0123456789') - set(expression)
    candidates = sorted(candidates)
    expression = expression.replace('=', '==')
    for x in candidates:
        t = expression.replace('X', x)
        if eval(t):
            return int(x)
    return -1
