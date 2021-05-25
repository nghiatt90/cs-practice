# https://codelearn.io/training/detail/29501
def nextNumber(n):
    set_bits = bin(n).count('1')
    nbits = len(bin(n)) - 2
    
    for i in range(nbits):
        if n & (1 << i):
            n ^= (1 << i)
            break
            
#     print(n)
    for j in range(i+1, nbits+1):
        n ^= (1 << j)
        if n & (1 << j):
            for k in range(j-i - 1):
                n |= (1 << k)
            return n
