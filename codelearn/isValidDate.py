# https://codelearn.io/training/detail/23051
import datetime

def isValidDate(d, m, y):
    try:
        datetime.date(y, m, d)
        return True
    except:
        return False
