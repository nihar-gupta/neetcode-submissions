class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            n = len(grid)
            m = len(grid[0])
            return x>=0 and y>=0 and x<n and y<m

        n = len(grid)
        m = len(grid[0])

        c = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cc = 0
                    if valid(i-1, j) is False or grid[i-1][j] == 0:
                        cc += 1
                    
                    if valid(i+1, j) is False or grid[i+1][j] == 0:
                        cc += 1
                    
                    if valid(i,j-1) is False or grid[i][j-1] == 0:
                        cc += 1
                    
                    if valid(i, j+1) is False or grid[i][j+1] == 0:
                        cc += 1
                    
                    c += cc
        return c
                        
        