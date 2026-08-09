class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = m*m
        p1 = 0
        p2 = 0
        for i in range(m):
            for j in range(m):
                p1 += grid[i][j]
                p2 += (grid[i][j]*grid[i][j])
        
        p3 = n*(n+1)//2
        p4 = n*(n+1)*(2*n+1)//6

        x = (((p4-p2)//(p3-p1)) - p1+p3)//2
        y = x - p3+p1
        return [y,x]



        