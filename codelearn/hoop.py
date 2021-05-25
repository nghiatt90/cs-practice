# https://codelearn.io/training/detail/23351
def hoop(n, m, turns):
    ans = []
    for i, v in enumerate(turns):
        correct = i+1 if (i+1)%3 and (i+1)%7 else 0
        if v != correct:
            ans.append(i%n + 1)
    return ans
