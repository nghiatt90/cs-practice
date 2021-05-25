# https://codelearn.io/training/detail/6167
def calculateElectricBill(n):
    s = 1000
    if n <= 50:
        return s + n * 230
    n -= 50
    s += 50 * 230
    if n <= 50:
        return s + n * 480
    n -= 50
    s += 50 * 480
    if n <= 49:
        return s + n * 700
    n -= 49
    s += 49 * 700
    return s + n*900
