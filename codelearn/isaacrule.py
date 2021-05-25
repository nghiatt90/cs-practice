# https://codelearn.io/training/detail/3424
def isaacRule(steps, number):
    queue = [number]
    while steps:
        next_queue = set()
        for n in queue:
            next_queue.add(n*2)
            t = (n - 1) // 3
            if 1 < t and t % 2 and t*3+1 == n:
                next_queue.add(t)
        steps -= 1
        queue = next_queue
    return len(queue)

