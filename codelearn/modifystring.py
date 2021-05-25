# https://codelearn.io/training/detail/118962
def modifyString(s):
    dup_cnt = 1
    cnt = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dup_cnt += 1
        else:
            dup_cnt = 1
        if dup_cnt == 3:
            cnt += 1
            dup_cnt = 1
    return cnt

