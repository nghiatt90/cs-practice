# https://codelearn.io/training/detail/34644
import re

def fileName(s):
    ans = 0
    for sub in re.findall('x{3,}', s):
        ans += len(sub) - 2
    return ans
