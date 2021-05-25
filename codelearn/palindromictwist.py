# https://codelearn.io/training/detail/34550
def palindromicTwist(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j] and abs(ord(s[i]) - ord(s[j])) != 2:
            return False
        i += 1
        j -= 1
    return True
