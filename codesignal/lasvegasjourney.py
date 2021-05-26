# https://app.codesignal.com/challenge/RGyYYmQtrD6wGtB9h
A, R, s = eval(dir()[0])
I = 9e9
n = len(A)
A = [0] * n + A
for i in range(n-1, 0, -1):
    A[i] = max(A[i*2], A[i*2+1])

i = j = 0
D = L = I
for a, b in R:
    l = n + a
    r = n + b + 1
    m = 0
    while l < r:
        if l & 1:
            m = max(m, A[l])
            l += 1
        if r & 1:
            r -= 1
            m = max(m, A[r])
        l >>= 1
        r >>= 1

    x = abs(m - s)
    if x < D or x == D and b - a < L:
        D = x
        L = b - a
        j = i
    i += 1
return j
    

# class SegmentTreeMax(object):
#     def __init__(self, arr):
#         self.n = len(arr)
#         self.tree = [0] * (2*self.n)
#         for i in range(self.n):
#             self.tree[self.n + i] = arr[i]
#         self.build()
    
#     def build(self):
#         for i in range(self.n - 1, 0, -1):
#             self.tree[i] = max(self.tree[i<<1], self.tree[i<<1|1])
    
#     def update(self, i, value):
#         t = self.n + i
#         self.tree[t] = value
#         while t > 1:
#             self.tree[t>>1] = max(self.tree[t], self.tree[t^1])
#             t >>= 1
    
#     def query(self, l, r):
#         res = -float('inf');
#         l += self.n
#         r += self.n
#         while l < r:
#             if l & 1:
#                 res = max(res, self.tree[l])
#                 l += 1
#             if r & 1:
#                 r -= 1
#                 res = max(res, self.tree[r])
#             l >>= 1
#             r >>= 1
#         return res

# def lasVegasJourney(arr, ranges, standard):
#     tree = SegmentTreeMax(arr)
#     best_id = -1
#     best_diff = float('inf')
#     best_len = float('inf')
#     for i, rng in enumerate(ranges):
#         l, r = rng
#         max_in_range = tree.query(l, r+1)
#         diff = abs(max_in_range - standard)
#         if diff < best_diff or diff == best_diff and r - l + 1 < best_len:
#             best_diff = diff
#             best_len = r - l + 1
#             best_id = i
#     return best_id
