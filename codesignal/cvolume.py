# https://app.codesignal.com/challenge/5KoJvjuBKSeBwWe54
cVolume = lambda r, l, h: r and (r*r * math.acos(1 - h/r) - (r - h) * (2*r*h - h*h) ** .5) * l
