# https://codelearn.io/training/detail/46211
def smallestComponent(matrix):
    r, c = len(matrix), len(matrix[0])
    m = ['?' * (c+2)]
    for row in matrix:
        m.append('?%s?' % row)
    m += ['?' * (c+2)]
    checked = [[False] * (c+2) for _ in range(r+2)]
    
    def bfs(m, i, j):
#         print(f'BFS: {i} {j}')
        res = 1
        checked[i][j] = True
        for v, h in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if not checked[i+v][j+h] and m[i+v][j+h] == m[i][j]:
                res += bfs(m, i+v, j+h)
        return res
    
    min_size = 1 << 20
    for i in range(1, r+1):
        for j in range(1, c+1):
            if checked[i][j]: continue
#             print('=' * 20)
            size = bfs(m, i, j)
            if size < min_size:
                min_size = size
#                 print(i, j, size)
    return min_size
