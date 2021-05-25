# https://codelearn.io/training/detail/43148
def checksum_part1(barcode):
    multiplier = 3
    s = 0
    while barcode:
        digit = barcode % 10
        barcode //= 10
        s += digit * multiplier
        multiplier = 1 if multiplier == 3 else 3
    return (s+9)//10*10 - s
