# https://codelearn.io/training/detail/3922
from string import ascii_lowercase

def cipher26(message):
    int2char = ascii_lowercase
    char2int = dict(zip(ascii_lowercase, range(26)))
    
    res = ''
    cur = 0
    for char in message:
        x = char2int[char] - cur
        if x < 0:
            x += 26
        res += int2char[x]
        cur += x
    return res
        
