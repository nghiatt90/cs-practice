# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_area = min(height[l], height[r]) * r
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
        
        return max_area

assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
