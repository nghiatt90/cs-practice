def missingNumber(arr):
    """https://codelearn.io/training/detail/34744"""
    return sum(range(len(arr) + 2)) - sum(arr) 
