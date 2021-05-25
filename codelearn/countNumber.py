# https://codelearn.io/training/detail/128608
def countNumber(x):
    sqrt = int(x ** .5)
    base_digits = set()
    t = x
    cnt = 0
    while t:
        base_digits.add(t%10)
        t //= 10
    for i in range(1, sqrt+1):
        if x%i:
            continue
        for d in set((i, x//i)):
            t = d
            while t:
                if t%10 in base_digits:
                    cnt += 1
                    break
                t //= 10
    return cnt
