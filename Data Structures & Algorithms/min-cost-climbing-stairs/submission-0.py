class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def solve(cost, i):
        #     if i >= len(cost):
        #         return 0
            
        #     return cost[i] + min(solve(cost, i+1), solve(cost, i+2))
        # return min(solve(cost, 0), solve(cost, 1))

        n = len(cost)
        dp = [0 for i in range(n+2)]
        dp[n] = 0
        dp[n+1] = 0

        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])
        