# https://codelearn.io/training/detail/34621
def compareSumOfDigits(s):
    sum_ = 0
    for i in s:
        d = int(i)
        sum_ += d if d % 2 else -d
    return sum_
