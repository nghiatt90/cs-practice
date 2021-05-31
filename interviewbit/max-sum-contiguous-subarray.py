# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, arr):
        
        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i, n in enumerate(arr[1:], 1):
            dp[i] = max(n, dp[i-1]+n)
        
        return max(dp)
