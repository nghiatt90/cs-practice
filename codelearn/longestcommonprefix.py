# https://codelearn.io/training/detail/6924
def longestCommonPrefix(array):
    if not array:
        return ''
    lens = [len(a) for a in array]
    for i in range(min(lens)):
        if any(a[i] != array[0][i] for a in array):
            break
    else:
        i += 1
    return array[0][:i]
