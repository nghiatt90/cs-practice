# https://codelearn.io/training/detail/46716
def minesweeper(matrix):
    r, c = len(matrix), len(matrix[0])
    m = [[False] * (c+2)]
    for row in matrix:
        m.append([False] + row + [False])
    m += [[False] * (c+2)]
    
    res = [[0] * (c+2) for _ in range(r+2)]
    for i in range(1, r+1):
        for j in range(1, c+1):
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    res[i][j] += m[i+ii][j+jj]
            res[i][j] -= m[i][j]
    return [row[1:-1] for row in res[1:-1]]
