# https://codelearn.io/training/detail/27811
def powersOfTwo(k, arr):
    a = set(arr)
    for i in range(k+1):
        if 1 << i not in a:
            return 1 << i
    return 0

