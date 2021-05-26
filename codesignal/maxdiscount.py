# https://app.codesignal.com/challenge/HAa3E3KifJqEXotNt
def maxDiscount(p):
    m = [-1] * len(p)
    def dp(a, l):
        if l >= len(a): return 0
        if len(a) - l < 3:
            m[l] = 0
            return 0
        if m[l] >= 0: return m[l]
        m[l] = max(min(a[l:l+3])+dp(a, l + 3), dp(a, l + 1))
        return m[l]
    dp(p, 0)
    return m[0]

