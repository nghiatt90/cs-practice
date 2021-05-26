class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        rows, cols = len(A), len(A[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        current_direction = 0
        current_x, current_y = 0, -1
        remaining = rows * cols
        ans = []
        
        while remaining:
            while (
                top <= current_x + directions[current_direction][0] <= bottom
                and left <= current_y + directions[current_direction][1] <= right
            ):
                current_x += directions[current_direction][0]
                current_y += directions[current_direction][1]
                ans.append(A[current_x][current_y])
                remaining -= 1
            
            if current_direction == 0:
                top += 1
            elif current_direction == 1:
                right -= 1
            elif current_direction == 2:
                bottom -= 1
            else:
                left += 1
            current_direction = (current_direction + 1) % 4
        
        return ans
