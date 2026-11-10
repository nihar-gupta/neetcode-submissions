class Solution:
    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        def valid(x, y):
            return x>=0 and y>=0 and x<len(a) and y<len(a[0])

        if a[0][0] == 1 or a[-1][-1] == 1: return 0
        n = len(a)
        m = len(a[0])
        dp = [[0 for i in range(m)] for j in range(n)]

        dp[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if (i != 0 or j != 0) and a[i][j] == 0:
                    c = 0
                    if valid(i-1, j):
                        c+=dp[i-1][j]
                    if valid(i, j-1):
                        c+=dp[i][j-1]
                    dp[i][j] = c
        print(dp)
        return dp[-1][-1]
                    

        




        