# https://codelearn.io/training/detail/29500
def snail_trip(h, d, n):
    if h == 0:
        return 0
    if h <= d:
        return 1
    every_day = d - n
    nrof_day = (h - d + every_day - 1) // every_day
    return nrof_day + 1
