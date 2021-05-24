def decipher(cipher):
    """https://codelearn.io/training/detail/3920"""
    res = ''
    while cipher:
        if cipher[0] == '9':
            res += chr(int(cipher[:2]))
            cipher = cipher[2:]
        else:
            res += chr(int(cipher[:3]))
            cipher = cipher[3:]
    return res
