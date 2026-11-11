class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            return x>=0 and y>=0 and x<len(grid) and y<len(grid[0])
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                right = float('inf')
                if valid(i, j-1):
                    right = grid[i][j-1]
                
                up = float('inf')
                if valid(i-1, j):
                    up = grid[i-1][j]
                
                if i != 0 or j != 0:
                    grid[i][j] = grid[i][j] + min(right, up)
        return grid[-1][-1]
        