# https://app.codesignal.com/challenge/SamFd9tZzgXQwm5Sp
m = eval(dir()[0])[0]
if not m[0]:
    return 0

r = range
n = [
    [1, 2, 3, 6],
    [0, 2, 3, 4, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 2, 4],
    [1, 3, 6],
    [1, 2],
    [0, 2, 4],
    list(r(7))
]
c = [
    [0], [1], [2], [3],
    [0, 2],
    [0, 3],
    [1, 3],
    []
]

dp = [sum([m[i][0] for i in c[j]]) for j in r(8)]

for i in r(1, len(m[0])):
    dp = [max(dp[k] for k in n[j]+[7]) + sum([m[k][i] for k in c[j]]) for j in r(8)]

return max(dp)
