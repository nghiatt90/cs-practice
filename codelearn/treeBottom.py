# https://codelearn.io/training/detail/5089
def treeBottom(tree):
    ans = 0
    target_depth = 0
    cur_depth = -1
    cur_val = 0
    for c in tree:
        if c == '(':
            cur_depth += 1
        elif c == ')':
            cur_depth -= 1
        elif c == ' ':
            if cur_depth == target_depth:
                ans += cur_val
            elif cur_depth > target_depth:
                ans = cur_val
                target_depth = cur_depth
            cur_val = 0
        else:
            cur_val = cur_val * 10 + int(c)
    return ans
