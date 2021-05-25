# https://codelearn.io/training/detail/9049
def cyclicSequence(sequence):
    m = min(sequence)
    start = sequence.index(m)
    l = len(sequence)
    return all(sequence[(start+i)%l] > sequence[(start+i-1)%l] for i in range(1, l))
