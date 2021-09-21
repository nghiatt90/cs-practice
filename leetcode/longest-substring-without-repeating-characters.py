# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        max_len = 0
        curr_len = 0
        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= i - curr_len:
                # Duplicate
                max_len = max(max_len, curr_len)
                curr_len = i - last_seen[c]
            else:
                curr_len += 1
            last_seen[c] = i
        return max(max_len, curr_len)
