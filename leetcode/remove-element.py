# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        end = len(nums) - 1
        while end >= 0 and nums[end] == val:
            end -= 1
        for i, n in enumerate(nums):
            if i >= end:
                break
            if n == val:
                nums[i], nums[end] = nums[end], nums[i]
                while end >= 0 and nums[end] == val:
                    end -= 1
        return end + 1
