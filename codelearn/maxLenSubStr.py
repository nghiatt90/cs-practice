def maxLenSubStr(s):
    """https://codelearn.io/training/detail/4540"""
    S = set(s)
    m = 0
    for i in S:
        m = max(m, s.rfind(i) - s.find(i))
    return m + 1
