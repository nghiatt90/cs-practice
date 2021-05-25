# https://codelearn.io/training/detail/128654
def sortedArray(arr):
    x = sorted(arr)
    return sum(1 for i in range(len(arr)) if arr[i] != x[i]) in [0, 2]
