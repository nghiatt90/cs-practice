# https://codelearn.io/training/detail/20538
def consensus(candidate_positions):
    l = len(candidate_positions[0])
    cnt = 1
    for i in range(l):
        a = [x[i] for x in candidate_positions]
        if all(c=='?' for c in a):
            cnt *= 2
        if 'Y' in a and 'N' in a:
            return 0
    return cnt
