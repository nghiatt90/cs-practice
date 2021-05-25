# https://codelearn.io/training/detail/42107
def isAlmostLucky(n):
    queue = [4, 7]
    while queue[0] <= n:
        k = queue.pop(0)
        if n % k == 0:
            return True
        queue.append(k*10 + 4)
        queue.append(k*10 + 7)
    return False
