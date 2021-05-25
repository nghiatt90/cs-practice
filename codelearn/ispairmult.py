# https://codelearn.io/training/detail/29324
def isPairMult(arr, n):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]*arr[j] == n:
                return True
    return False
