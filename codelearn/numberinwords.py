# https://codelearn.io/training/detail/3419
def numberInWords(n):
    if n > 1e6 or n <= 0:
        while True:
            pass
    if n == int(1e6):
        return 'One million'

    digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    def rec(x, sep='-'):
        if x < 10:
            return digits[x]
        elif x < 20:
            return teens[x-10]
        elif x < 100:
            ten = x // 10
            digit = x % 10
            ret = tens[ten]
            if digit > 0:
                ret += sep + digits[digit]
            return ret
        elif x < 1000:
            hundred = x // 100
            ret = digits[hundred] + ' hundred'
            ret += ' ' + rec(x % 100)
            return ret.strip()
        else:
            thousand = x // 1000
            ret = rec(thousand, ' ') + ' thousand'
            ret += ' ' + rec(x % 1000)
            return ret.strip()
    
    return rec(n).capitalize()

