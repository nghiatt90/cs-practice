# https://codelearn.io/training/detail/33048
def chainNames(names):
    def rec(cur_ans, names):
#         print(f'rec({cur_ans}, {names})')
        if not names or len(names) == 0:
            return cur_ans
        for i in range(len(names)):
            if names[i][0].lower() == cur_ans[-1][-1]:
                new_names = names[:i] + names[i+1:]
                a = rec(cur_ans + [names[i]], new_names)
                if a:
                    return a
        return False
    for i, name in enumerate(names):
        a = rec([name], names[:i] + names[i+1:])
        if a:
            return a
    raise ValueError()
