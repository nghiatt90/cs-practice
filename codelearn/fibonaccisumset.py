# https://codelearn.io/training/detail/9302
def fibonacciSumSet(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    fib = fib[::-1]
    
    ans = []
    while n:
        for i in fib:
            if i <= n:
                n -= i
                ans.append(i)
                break
    return ans[::-1]
