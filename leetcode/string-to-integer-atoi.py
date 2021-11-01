# https://leetcode.com/problems/string-to-integer-atoi/

import re

class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        m = re.search('^ *([+-]?\d+)', s)
        if not m:
            return 0
        num = int(m.group(1))
        
        return sorted([-(1 << 31), num, (1 << 31) - 1])[1]
