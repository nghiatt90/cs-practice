# https://codelearn.io/training/detail/169788
def stringAB(n, k):
    ans = []
    for mask in range(1 << n):
        s = bin(mask)[2:].zfill(n)
        if s.find('0'*k) == s.rfind('0'*k) >= 0:
            ans.append(s.replace('0', 'A').replace('1', 'B'))
    return ans
