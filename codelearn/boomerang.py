# https://codelearn.io/training/detail/16455
def boomerang(arr):
    cnt = 0
    for i in range(2, len(arr)):
        cnt += 1 if arr[i] == arr[i-2] != arr[i-1] else 0
    return cnt
