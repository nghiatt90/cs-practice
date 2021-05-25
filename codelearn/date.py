# https://codelearn.io/training/detail/33302
import datetime

def date(d, m):
    x = datetime.date(2009, m, d)
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x.weekday()]
