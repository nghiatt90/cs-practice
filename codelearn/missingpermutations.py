# https://codelearn.io/training/detail/42237
import itertools

def missingPermutations(permutationList):
    s = sorted(permutationList[0])
    res = []
    for p in itertools.permutations(s):
        ps = ''.join(p)
        if ps not in permutationList:
            res.append(ps)
    return res
