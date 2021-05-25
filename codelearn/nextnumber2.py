# https://codelearn.io/training/detail/40488
def nextNumber2(arr):
    l = len(arr)
    if not l:
        return arr
    if l == 1:
        if arr[0] == 1:
            return [1, arr[0]]
        else:
            return [1, 1, arr[0]-1]

    arr = [0] * 2 + arr
    if l % 2:
        l += 1
        arr += [0]

    arr[-2] -= 1
    arr[-1] += 1
    
    to_be_offed = arr[-2]
    arr[-3] -= 1
    arr[-2] = 1
    arr.append(to_be_offed)
    
    while arr[0] <= 0:
        arr.pop(0)
    res = [arr.pop(0)]
    
    add_next = False
    for i in arr:
        if add_next:
            add_next = False
            res[-1] += i
            continue
        if i == 0:
            add_next = True
        else:
            res.append(i)
    
    return res
