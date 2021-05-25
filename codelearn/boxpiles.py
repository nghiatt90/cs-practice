# https://codelearn.io/training/detail/44223
def boxPiles(a):
    a.sort()
    piles = []
    for s in a:
        for p in piles:
            if len(p) <= s:
                p.append(s)
                break
        else:
            piles.append([s])
    return len(piles)
