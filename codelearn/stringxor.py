# https://codelearn.io/training/detail/28141
def stringXor(s, t):
    return bin(int(s,2)^int(t,2))[2:].rjust(max(len(s), len(t)), '0')
