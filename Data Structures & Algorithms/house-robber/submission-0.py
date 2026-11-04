class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(a, i, take):
            if i == len(a):
                return 0
            
            if take:
                p1 = a[i] + solve(a, i+1, False)
                p2 = solve(a, i+1, True)
                return max(p1, p2)
            else:
                p2 = solve(a, i+1, True)
                return p2
        #return solve(nums, 0, True)
        
        n = len(nums)
        dp = [[0 for i in range(2)]for j in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                if j:
                    p1 = nums[i] + dp[i+1][0]
                    p2 = dp[i+1][1]
                    dp[i][j] = max(p1,p2)
                else:
                    dp[i][j] = dp[i+1][1]
        return dp[0][1]




