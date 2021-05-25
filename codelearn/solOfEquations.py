# https://codelearn.io/training/detail/296819
def solOfEquations(k, a, b, c):
    k -= (a+b+c)
    if k == 0:
        return 1
    if k < 0:
        return 0

    return (k+1 if k%2==0 else k+2)*((k + 2) // 2)
