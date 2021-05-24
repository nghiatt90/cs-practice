# https://codelearn.io/training/detail/3429
def differentSquares(m):
    cnt = 0
    r, c = len(m)-1, len(m[0])-1
    for k in range(r*c):
        i, j = k // c, k % c
        for x in range(k+1, r*c):
            ii, jj = x // c, x % c
            if m[i][j] == m[ii][jj] and m[i][j+1] == m[ii][jj+1] and m[i+1][j] == m[ii+1][jj] and m[i+1][j+1] == m[ii+1][jj+1]:
                break
        else:
            cnt += 1
    return cnt
