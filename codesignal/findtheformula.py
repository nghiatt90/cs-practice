# https://app.codesignal.com/challenge/PR8br4c5qagRqmoab
def findTheFormula(s):
    a, b, c = s
    k = (c - b) // (b - a)
    q = c - k * b
    r = "-n" if k == -1 else "n" if k == 1 else str(k) + "n"
    m = "+" if q > 0 else ""
    t = str(q) if q != 0 else ""
    return r + m + t
    
    


