# https://codelearn.io/training/detail/3440
from string import ascii_lowercase as alphabet

def questionCorrection(x):
    chars = alphabet + '0123456789,?'
    
    # space
    x = x.strip()
    if x[-1] != '?':
        x += '?'

    s = [' ']
    for i in range(len(x)):
        c = x[i]
        if c.lower() not in chars:
            # common
            c = ' '
        elif c == '?' and i != len(x) - 1:
            c = ' '
        
        if not s[-1].isalnum() and c in ' ,?':
            s.pop()
            if c != ' ' and not s[-1].isalnum():
                s.pop()

        s.append(c.lower())
        if c == ',':
            s.append(' ')
    
    if s[0] == ' ':
        s.pop(0)
    s[0] = s[0].upper()
    return ''.join(s)


        
    

