# https://codelearn.io/training/detail/44210
def truncateString(s):
    if not s:
        return s
    if int(s[0]) % 3 == 0:
        return truncateString(s[1:])
    if int(s[-1]) % 3 == 0:
        return truncateString(s[:-1])
    if int(s[0] + s[-1]) % 3 == 0:
        return truncateString(s[1:-1])
    return s
