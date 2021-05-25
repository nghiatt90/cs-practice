# https://app.codesignal.com/challenge/xunq4T96b3fY54Wif
def triangularity(s):
    s.sort()
    return any(s[i]+s[i+1]>s[i+2] for i in range(len(s) - 2))


