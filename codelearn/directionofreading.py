# https://codelearn.io/training/detail/5766
def directionOfReading(numbers):
    l = len(numbers)
    ans = []
    for i in range(l):
        v = 0
        for j in range(l):
            v = v*10 + numbers[j]%10
            numbers[j] //= 10
        ans.append(v)
    return ans[::-1]
