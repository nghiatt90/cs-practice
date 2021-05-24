def arrayMaxConsecutiveSum(inputArray, k):
    """https://codelearn.io/training/detail/3621"""
    pre = [0]
    for i in inputArray:
        pre.append(pre[-1] + i)
    max_ = 0
    for i in range(k, len(pre)):
        max_ = max(max_, pre[i] - pre[i-k])
    return max_ 
