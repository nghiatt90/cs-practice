# https://app.codesignal.com/challenge/7mZGy8xF3exJveRuj
def Square_Check(p):
    a = sorted([(p[0] - p[x])**2 + (p[1] - p[x+1])**2 for x in range(2, 8, 2)])
    return a[0] == a[1] < a[2]
    

