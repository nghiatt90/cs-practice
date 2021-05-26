# https://app.codesignal.com/challenge/RWQS5cCEodqSWx4bR
import itertools as I
stringsRearrangement = lambda a: sum(1 for X in list(I.permutations(a)) if sum(1 for i in range(len(X) - 1) if sum(1 for x, y in zip(X[i], X[i + 1]) if x != y) != 1) == 0) != 0
