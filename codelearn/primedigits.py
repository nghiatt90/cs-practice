# https://codelearn.io/training/detail/31437
def primeDigits(n):
    is_prime = lambda x: all(x%i for i in range(2, int(x**.5)+1))
    cnt = 0
    queue = [2,3,5,7]
    while True:
        x = queue.pop(0)
        if x > n:
            return cnt
        # print(x, is_prime(x))
        if is_prime(x):
            cnt += 1
        queue.append(x*10+2)
        queue.append(x*10+3)
        queue.append(x*10+5)
        queue.append(x*10+7)
