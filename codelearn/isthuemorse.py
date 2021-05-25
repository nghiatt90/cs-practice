# https://codelearn.io/training/detail/20149
def isThueMorse(seq):
    x = [0]
    while True:
        for i in range(len(x)):
            if i < len(seq) and x[i] != seq[i]:
                return False
            if i == len(seq):
                return True
            x.append(1-x[i])
