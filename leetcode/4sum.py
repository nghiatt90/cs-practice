# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        last = {}
        for i, n in enumerate(nums):
            last[n] = i
        
        ans = set()
        L = len(nums)
        for a in range(L):
            for b in range(a+1, L):
                for c in range(b+1, L):
                    aux = target - nums[a] - nums[b] - nums[c]
                    d = last.get(aux, -1)
                    if d > c:
                        ans.add(tuple(sorted((nums[a], nums[b], nums[c], aux))))
                        
        return ans
