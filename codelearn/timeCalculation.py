# https://codelearn.io/training/detail/6342
def timeCalculation(s):
    h = s // 3600
    s %= 3600
    d = s // 60
    s %= 60
    return f'{h:02d}:{d:02d}:{s:02d}'
