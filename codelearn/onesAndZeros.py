# https://codelearn.io/training/detail/16902
def onesAndZeros(s):
    ones = s.count('1')
    zeros = len(s) - ones
    return abs(zeros - ones)
