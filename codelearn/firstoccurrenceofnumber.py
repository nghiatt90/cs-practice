# https://codelearn.io/training/detail/34400
def firstOccurrenceOfNumber(n):
    s = ''.join(str(i) for i in range(n+1))
    return s.find(str(n))
