# https://codelearn.io/training/detail/5170
def regularBracketSequence(sequence):
    s = 0
    for i in sequence:
        s += 1 if i == '(' else -1
        if s < 0:
            return False
    return s == 0
