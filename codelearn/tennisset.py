# https://codelearn.io/training/detail/4438
def tennisSet(score1, score2):
    win, loss = max(score1, score2), min(score1, score2)
    return win == 6 and loss < 5 or win == 7 and 4 < loss < 7
