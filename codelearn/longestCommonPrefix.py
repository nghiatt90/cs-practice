# https://codelearn.io/training/detail/6871
def longestCommonPrefix(a):
    if not a:
        return ''
    lcm = ''
    i = 0
    for i in range(len(a[0])):
        c = a[0][i]
        for j in range(1, len(a)):
            if i >= len(a[j]) or a[j][i] != c:
                return lcm
        lcm += c
    return lcm
