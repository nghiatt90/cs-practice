# https://codelearn.io/training/detail/49069
def charLocation(tex, wid, ch):
    ans = []
    for i, c in enumerate(tex):
        if c != ch:
            continue
        r = i // wid
        c = i % wid
        if r & 1:
            c = wid - c - 1
        ans.append([r, c])
    return sorted(ans)
