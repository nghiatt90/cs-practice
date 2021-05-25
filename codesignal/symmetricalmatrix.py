# https://app.codesignal.com/challenge/q5WHJQTyiL4XERsBL
def symmetricalMatrix(n, a):
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i][j] != a[j][i]:
                return False
    return True
