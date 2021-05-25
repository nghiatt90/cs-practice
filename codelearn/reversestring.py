# https://codelearn.io/training/detail/34794
def reverseString(str1):
    s = ''
    for c in str1[::-1]:
        if c.isalpha():
            s += c
    return s
