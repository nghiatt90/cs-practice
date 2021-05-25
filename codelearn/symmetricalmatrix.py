# https://codelearn.io/training/detail/9484
def symmetricalMatrix(m):
    for i in range(len(m)):
        for j in range(i+1, len(m[0])):
            if m[i][j] != m[j][i]:
                return False
    return True
