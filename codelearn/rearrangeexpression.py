# https://codelearn.io/training/detail/42091
def rearrangeExpression(s):
    s = s.split('+')
    s.sort()
    return '+'.join(s)
