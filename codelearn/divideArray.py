# https://codelearn.io/training/detail/35178
def divideArray(a, b):
    return sum(all(x%y==0 for y in b) for x in a)
