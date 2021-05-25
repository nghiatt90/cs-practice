# https://codelearn.io/training/detail/121022
def turnsOnRoad(x, y):
    if (x, y) in [(0,0), (1,0)]:
        return 0
    if x >= 1 and (1-x) < y <= x:
        return (x-1)*4+1
    if y >= 1 and -y <= x < y:
        return (y-1)*4+2
    if x <= -1 and x <= y < -x:
        return (-x-1)*4+3
    return (-y-1)*4+4
