# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        suppliments = {}
        for i, n in enumerate(nums):
            if n in suppliments:
                return [suppliments[n], i]
            suppliments[target - n] = i
        return None, None
