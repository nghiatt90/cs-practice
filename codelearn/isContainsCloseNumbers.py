def isContainsCloseNumbers(nums, k):
    """https://codelearn.io/training/detail/7016"""
    pos = {}
    for i, v in enumerate(nums):
        if v in pos and i - pos[v] <= k:
            return True
        pos[v] = i
    return False
