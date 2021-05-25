# https://codelearn.io/training/detail/34446
def diverseString(s):
    if len(s) != len(set(s)):
        return False
    s = sorted(s)
    return all(ord(s[i]) - ord(s[i-1]) == 1 for i in range(1, len(s)))
