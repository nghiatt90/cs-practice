# https://codelearn.io/training/detail/5050
def cyclicString(s):
    for i in range(1, len(s)):
        sub = s[:i]
        ss = sub * (len(s) // i + 1)
        if s in ss:
            return i
    return len(s)

