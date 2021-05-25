# https://codelearn.io/training/detail/34519
from collections import Counter
from string import ascii_uppercase as chars

def longestSubsequence(s, k):
    cnt = Counter(s)
    return k * min(cnt[c] for c in chars[:k])
