# https://codelearn.io/training/detail/18479
def onesAndZeros4(s):
    s = list(s)
    cnt = 0
    for i in range(1, len(s)-1):
        if s[i] == '1' and s[i-1] == s[i+1] == '0':
            s[i+1] = '1'
            cnt += 1
    return cnt
            
