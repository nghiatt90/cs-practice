# https://codelearn.io/training/detail/128702
def discount(p, q):
    if p < 10:
        return p
    n = p
    min_n = p - q
    k = 0
    
    while True:
        k += 1
#         print(n, k)
        if 10**k > p:
            break
        x = p % (10**k)
        if x == 10**k - 1:
            continue
        y = p // (10**k) - 1
        next_n = y * (10**k) + (10**k) - 1
        if next_n < min_n:
            break
        n = next_n
        
    return n
