# https://codelearn.io/training/detail/3417
def digitsProduct(product):
    for i in range(1, 10000):
        x = i
        p = 1
        while x:
            p *= x % 10
            x //= 10
        if p == product:
            return i
    return -1
