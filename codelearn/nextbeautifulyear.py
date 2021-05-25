# https://codelearn.io/training/detail/42120
def nextBeautifulYear(y):
    while True:
        y += 1
        if len(set(str(y))) == len(str(y)):
            return y
