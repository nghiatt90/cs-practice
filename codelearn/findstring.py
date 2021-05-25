# https://codelearn.io/training/detail/35061
def findString(s, p):
    import re
    return len(re.findall(f'(?={p})', s))
