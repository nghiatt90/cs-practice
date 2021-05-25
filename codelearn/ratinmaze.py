# https://codelearn.io/training/detail/76224
from collections import namedtuple
from heapq import heappop, heappush, heapify

def ratInMaze(m):
    Direction = namedtuple('Direction', ['y', 'x', 'char'])
    directions = (
        Direction( 0,  1, 'D'),
        Direction(-1,  0, 'L'),
        Direction( 1,  0, 'R'),
        Direction( 0, -1, 'U'),
    )
    n = len(m)
    visited = [[False]*n for _ in range(n)]
    ans = []
    
    def dfs(i, j, path):
        if 0 > i or n <= i or 0 > j or n <= j:
            return
        if visited[i][j] or m[i][j] == 0:
            return
        if i == j == n-1:
            ans.append(path)
            return
        visited[i][j] = True
        for d in directions:
            dfs(i+d.x, j+d.y, path+d.char)
        visited[i][j] = False
    
    dfs(0, 0, '')
    
    return sorted(ans)
