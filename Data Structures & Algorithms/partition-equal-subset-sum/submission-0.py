class Solution:
    def canPartition(self, a: List[int]) -> bool:

        def solve(a, i, target):
            if target < 0: return False
            if target == 0: return True
            if i==len(a):
                return False 
            
            nottake = solve(a, i+1, target)
            take = False
            if target - a[i] >=0 :
                take = solve(a, i+1, target-a[i])
            return nottake or take 
        
        

        s = sum(a)
        if s%2 != 0: return False 
        s = s//2

        #return solve(a, 0, s)
        n = len(a)
        dp = [[False for j in range(s+1)]for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True 
        
        for i in range(n-1, -1, -1):
            for j in range(1,s+1):
                if j-a[i] >= 0:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j-a[i]]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][s]

        