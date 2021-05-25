# https://codelearn.io/training/detail/42219
def prevPalindrome(x):
    if x < 11:
        return x - 1
    sx = list(str(x))
    
    if sx[0] == '1' and sx[-1] in '01' and all(i == '0' for i in sx[1:-1]):
        return '9' * (len(sx) - 1)
    
    l = len(sx)
    mid = (l+1) // 2
    best = (sx[:mid] + sx[mid-1::-1]) if l % 2 == 0 else (sx[:mid] + sx[mid-2::-1])
    if int(''.join(best)) < x:
        return ''.join(best)
    
    mid = l // 2
    offset = 1 - (l % 2)
#     print(f'offset {offset}')
    found = False
    for p in range((l+1) // 2):
#         print(p)
        l = mid - offset - p
        r = mid + p
#         print(l, r)
        if found:
            sx[r] = sx[l]
        elif sx[l] < sx[r]:
            sx[r] = sx[l]
            found = True
        elif sx[l] != '0':
            sx[r] = sx[l] = str(int(sx[l])-1)
            found = True
        else:
            sx[r] = sx[l] = '9'
    return ''.join(sx)
