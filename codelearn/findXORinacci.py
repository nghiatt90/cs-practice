# https://codelearn.io/training/detail/194822
def findXORinacci(a, b, n):
    d = {
        '00': '000',
        '01': '011',
        '10': '101',
        '11': '110',
    }
    a = bin(a)[2:].zfill(32)
    b = bin(b)[2:].zfill(32)
    n %= 3
    return int(''.join(d[a[i]+b[i]][n] for i in range(32)), 2)
