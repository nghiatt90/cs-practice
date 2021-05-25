# https://codelearn.io/training/detail/4976
def maximizeNumberRoundness(n):
    n = str(n)
    zero = 0
    nonzero = len(n) - 1
    ans = 0
    while zero < nonzero:
        if n[zero] == '0':
            while zero < nonzero and n[nonzero] == '0':
                nonzero -= 1
            if zero == nonzero:
                return ans    
            ans += 1
            nonzero -= 1
            # print('swap', zero, nonzero)
        zero += 1
    return ans

