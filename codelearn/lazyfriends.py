# https://codelearn.io/training/detail/44176
import bisect

def lazyFriends(houses, max_dist):
    l_index, r_index = {}, {}
    res = []
    for i, p in enumerate(houses):
        l_index[i] = bisect.bisect_left(houses, p - max_dist)
        r_index[i] = bisect.bisect_right(houses, p + max_dist)
        res.append(r_index[i] - l_index[i] - 1)
    return res
