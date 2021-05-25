# https://codelearn.io/training/detail/34417
def loveA(s):
    a = s.count('a')
    return min((a-1)*2+1, len(s))
