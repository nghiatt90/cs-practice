# https://codelearn.io/training/detail/51738
def brothersInTheBar(glasses, debug=False):
    def encode(s):
        l = []
        r = [-1]
        for c in s:
            if c != r[-1]:
                r.append(c)
                l.append(1)
            else:
                l[-1] += 1
        return r[1:], l
    glasses, code = encode(glasses)
    
    ans = 0
    changed = True
    
    def try_remove(b, l, i):
        nonlocal ans, changed
        if debug: print(f'try_remove({b}, {l}, {i})')
        b = list(b)
        l = list(l)
        if not b:
            if debug: print('Is this alright?')
            return b, l
        if l[i] < 3:
            if debug: print('Nothing to remove')
            return b, l
        ans += 1
        l[i] -= 3
        changed = True
        if l[i]:
            if debug: print('Remove, some remain')
            return b, l
        if i == 0 or i == len(b)-1 or b[i-1] != b[i+1]:
            if debug: print('Remove 1 element')
            b.pop(i)
            l.pop(i)
            return b, l
        if debug: print('Remove middle')
        l[i-1] += l[i+1]
        b.pop(i+1)
        b.pop(i)
        l.pop(i+1)
        l.pop(i)
        return try_remove(b, l, i-1)

    while changed:
        changed = False
        for i in range(len(glasses)):
            glasses, code = try_remove(glasses, code, i)
            if changed:
                break
        else:
            break
    return ans
