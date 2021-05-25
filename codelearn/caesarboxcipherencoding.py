# https://codelearn.io/training/detail/7663
def encode(s, i):
    return ''.join(''.join(s[j::i] for j in range(i)))

def caesarBoxCipherEncoding(message):
    l = len(message)
    cnt = 0
    for i in range(2, l):
        if l % i == 0 and encode(encode(message, i), i) == message:
            cnt += 1
    return cnt
