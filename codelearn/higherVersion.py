# https://codelearn.io/training/detail/3924
def higherVersion(v1, v2):
    v1 = [int(x) for x in v1.split('.')]
    v2 = [int(x) for x in v2.split('.')]
    for i in range(len(v1)):
        if v1[i] < v2[i]:
            return False
        if v1[i] > v2[i]:
            return True
    return False

