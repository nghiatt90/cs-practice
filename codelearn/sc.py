# https://codelearn.io/training/detail/35042
def sc(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = s[i].upper()
        elif s[i].isupper():
            s[i] = s[i].lower()
    return ''.join(s)
