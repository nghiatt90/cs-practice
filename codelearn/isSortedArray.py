def isSortedArray(arr):
    """https://codelearn.io/training/detail/23151"""
    return all(arr[i-1] <= arr[i] for i in range(1, len(arr)))
