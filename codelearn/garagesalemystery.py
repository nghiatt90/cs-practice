# https://codelearn.io/training/detail/51731
def garageSaleMystery(stickers, items):
    stickers.sort()
    prices = [0] * items
    k = 1
    while len(stickers) >= items:
        for i in range(items):
            prices[i] = k*stickers.pop() + prices[i]
        k *= 10
    i = -1
    while stickers:
        prices[i] = k*stickers.pop() + prices[i]
        i -= 1
    return sum(prices)
    
