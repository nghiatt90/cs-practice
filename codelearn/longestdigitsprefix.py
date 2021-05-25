# https://codelearn.io/training/detail/34448
def longestDigitsPrefix(s):
    for i in range(len(s)):
        if not s[i].isnumeric():
            return s[:i]
    return s
