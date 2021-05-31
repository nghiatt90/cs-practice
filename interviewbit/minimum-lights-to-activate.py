# https://www.interviewbit.com/problems/minimum-lights-to-activate/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, lights, power):
        i = 0
        cnt = 0
        while i < len(lights):
#             print(i)
            for j in range(
                min(i + power - 1, len(lights)-1),
                max(i - power, 0),
                -1
            ):
#                 print(f'  {j}')
                if lights[j]:
                    i = j + power
                    cnt += 1
                    break
            else:
                return -1
        return cnt
