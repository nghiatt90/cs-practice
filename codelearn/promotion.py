def promotion(x, y, s):
    """https://codelearn.io/training/detail/308256"""
    d = s // (x+y)
    return d * x + min(s-d*(x+y), x)
