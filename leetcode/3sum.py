# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        ans = set()
        
        for i in range(l):
            hash_set = set()
            for j in range(i+1, l):
                if -(nums[i] + nums[j]) in hash_set:
                    ans.add(tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])])))
                hash_set.add(nums[j])
        
        return [list(x) for x in ans]

assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
