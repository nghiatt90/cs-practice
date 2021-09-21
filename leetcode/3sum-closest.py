# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        assert len(nums) >= 3
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        L = len(nums)
        for i in range(L):
            l, r = 0, L - 1
            while l < i < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s == target:
                    return target
                if s < target:
                    l += 1
                else:
                    r -= 1
        return closest
