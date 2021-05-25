# https://codelearn.io/training/detail/42197
def clockRadian(t):
    h, m = [int(x) for x in t.split(':')]
    if h == 12:
        h = 0
    
    minute_hand = (24*m, 60*12)  # 2*pi/60 * m
    hour_hand = (120*h + 2*m, 60*12)  # 2*pi/12 * h + 2*pi/(60*12) * m
    
    gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
    
    numer = abs(minute_hand[0] - hour_hand[0])
    denom = minute_hand[1]
    g = gcd(numer, denom)
    numer //= g
    denom //= g
    if numer > denom:
        numer = 2*denom - numer
        
    if numer == 0:
        return '0'
    numer = '' if numer == 1 else str(numer)
    return f'{numer}pi/{denom}' if denom > 1 else 'pi'
