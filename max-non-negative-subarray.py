# https://www.interviewbit.com/problems/max-non-negative-subarray/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = -1
        max_length = -1
        start_index = -1
        
        current_sum = 0
        current_len = 0
        A.append(-1)
        for i, n in enumerate(A):
            if n < 0:
                if current_sum > max_sum or current_sum == max_sum and current_len > max_length:
                    max_sum = current_sum
                    max_length = current_len
                    start_index = i - current_len
                current_sum = current_len = 0
            else:
                current_sum += n
                current_len += 1
        return A[start_index:start_index+max_length]
