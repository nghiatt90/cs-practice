def oddNumbersBeforeZero(sequence):
    """https://codelearn.io/training/detail/32886"""
    cnt = 0
    for n in sequence:
        if n == 0:
            break
        cnt += n%2
    return cnt
