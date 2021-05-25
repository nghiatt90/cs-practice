# https://codelearn.io/training/detail/20545
def base26(n):
    if n < 26:
        return chr(n+97)
    return base26(n//26) + base26(n%26)

def conversion(a):
    s = [base26(x) for x in a]
    max_len = len(base26(max(a)))
    return base26(max_len-1) + ''.join(('a'*(max_len-len(ss))) + ss for ss in s)

