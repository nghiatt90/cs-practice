# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

key = {
    2: list('abc'),
    3: list('def'),
    4: list('ghi'),
    5: list('jkl'),
    6: list('mno'),
    7: list('pqrs'),
    8: list('tuv'),
    9: list('wxyz'),
}

def product(iter_1, iter_2):
    for i in iter_1:
        for j in iter_2:
            yield i + j

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        a = [key[int(c)] for c in digits]
        for l in a[1:]:
            a[0] = product(a[0], l)
        return list(a[0])
        


# In case you have to push a button more than 1 to type
# some characters, e.g. use "22" to get "b",
# the following code works.


# def build_dp_tables(max_consecutive_len):
#     dp_l3 = [None for _ in range(max(max_consecutive_len + 1, 4))]
#     dp_l3[1] = [(0,)]
#     dp_l3[2] = [(0, 0), (1,)]
#     dp_l3[3] = [(0, 0, 0), (0, 1), (1, 0), (2,)]
#     for i in range(4, len(dp_l3)):
#         dp_l3[i] = set().union(*(
#             product(dp_l3[1], dp_l3[i-1]),
#             product(dp_l3[2], dp_l3[i-2]),
#             product(dp_l3[3], dp_l3[i-3]),
#         ))

#     dp_l4 = [None for _ in range(max(max_consecutive_len + 1, 5))]
#     dp_l4[1] = [(0,)]
#     dp_l4[2] = [(0, 0), (1,)]
#     dp_l4[3] = [(0, 0, 0), (0, 1), (1, 0), (2,)]
#     dp_l4[4] = [(0, 0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 2), (1, 0, 0), (1, 1), (2, 0), (3,)]
#     for i in range(5, len(dp_l3)):
#         dp_l4[i] = set().union(*(
#             product(dp_l4[1], dp_l4[i-1]),
#             product(dp_l4[2], dp_l4[i-2]),
#             product(dp_l4[3], dp_l4[i-3]),
#             product(dp_l4[4], dp_l4[i-4]),
#         ))
#     return dp_l3, dp_l4


# def split(s):
#     """Split string into tuples (char, consecutive_length).
    
#     '222334' -> [(2, 3), (3, 2), (4, 1)]
#     """
#     c = s[0]
#     r = []
#     current = 0
#     for i in range(len(s)):
#         if s[i] != c:
#             r.append((int(c), i-current))
#             current = i
#             c = s[i]

#     r.append((int(c), len(s)-current))
#     return r            


# def mapping(k, l, dp_l3, dp_l4):
#     """Map tuple (char, consecutive_length) to list of possible combinations."""
#     chars = key[k]
#     dp = dp_l3 if len(chars) == 3 else dp_l4
#     ans = []
#     for tup in dp[l]:
#         s = ''.join(chars[i] for i in tup)
#         ans.append(s)
#     return tuple(ans)
        

# class Solution:
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if not digits:
#             return []
        
#         digits = split(digits)
#         max_consecutive_len = max(l for _, l in digits)
#         dp_l3, dp_l4 = build_dp_tables(max_consecutive_len)
        
#         a = [mapping(k, l, dp_l3, dp_l4) for k, l in digits]
#         for tup in a[1:]:
#             a[0] = list(product(a[0], tup))
#         return a[0]
