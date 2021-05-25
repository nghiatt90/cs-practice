# https://codelearn.io/training/detail/32900
def sumOfDigits2(n):
    from pprint import pprint
    digits = [int(x) for x in str(n)]
    s = sum(digits)
    dp = [[[0] * 10 for _ in range(len(digits)+1)] for _ in range(s+1)]
    for j in range(len(digits)+1):
        dp[0][j][0] = 1
    for i in range(1, s+1):
        for j in range(1, len(digits)+1):
            for k in range(10):
                if i-k < 0:
                    break
                dp[i][j][k] = sum(dp[i-k][j-1])
    
    a = sum(dp[s][len(digits)])
    l = 0
#     print(a)
    for j in range(len(digits)):
        s -= l
        a -= sum(dp[s][len(digits)-j][digits[j]+1:])
#         print(a)
        l = digits[j]
#     pprint(dp)
    
    return a
sumOfDigits2(111)
