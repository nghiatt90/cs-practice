def sumOfNumbers(arr, n):
    """https://codelearn.io/training/detail/53109"""
    return sum(s for s in range(1, n+1) if any(s % i == 0 for i in arr))
