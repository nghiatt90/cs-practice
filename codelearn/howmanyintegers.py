# https://codelearn.io/training/detail/32248
def howManyIntegers(n):
    queue = [4, 7]
    ans = 0
    while queue[0] < n:
        k = queue.pop(0)
        ans += 1
        queue.append(k*10 + 0)
        queue.append(k*10 + 4)
        queue.append(k*10 + 7)
    return ans
