# https://app.codesignal.com/challenge/83DLvfGhkw6q4wWTv
B, M, *c = eval(dir()[0])

L = len
Z = range
p, q = L(B), L(B[0])

Q = Z(-1, 2)
A = lambda x, y: [(x+i, y+j) for i in Q for j in Q if p > x+i >= 0 <= y+j < q]

def X(x, y):  # Reveal a cell
    if R[x][y] | F[x][y]:  # Already revealed or flagged
        return 1
    v = B[x][y]
    if v > 8:  # Hit a bomb
        return 0
    
    R[x][y] = 1
    if v:  # Normal cell (value >= 1)
        return 1
    
    # 0 cell
    w = 1
    for k in A(x, y):
        w *= X(*k)
    return w

R = [[0] * q for _ in Z(p)]  # Reveal state
F = [r[:] for r in R]  # Flag state
w = 1
for x, y, k in M:
    if k:  # Flag
        F[x][y] = 1 - F[x][y]
    else:  # Click
        if R[x][y]:  # Click on a revealed cell
            J = A(x, y)
            if sum(F[i][j] for i, j in J) == B[x][y]:  # Number of flags matches
                for k in J:
                    w *= X(*k)
        else:  # Click on hidden cell
            w *= X(x, y)
return [[],R][w]
