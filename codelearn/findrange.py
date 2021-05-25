# https://codelearn.io/training/detail/29216
def findRange(array, n):
    if n == array[0]:
        return True
    acc = [0]
    for x in array:
        acc.append(acc[-1] + x)
    for i in range(len(acc)):
        for j in range(i+1, len(acc)):
            if n == acc[j] - acc[i]:
                return True
    return False
