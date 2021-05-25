# https://codelearn.io/training/detail/45217
def is_palin(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def longestSubstr(s):
    if len(set(s)) == 1:
        return 0
    return len(s) - 1 if is_palin(s) else len(s)
