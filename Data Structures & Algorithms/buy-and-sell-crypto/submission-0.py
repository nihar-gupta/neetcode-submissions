class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rt = 0
        mi = prices[0]
        n = len(prices)
        for i in range(1, n):
            rt = max(rt, prices[i] - mi)
            mi = min(mi, prices[i])
        return rt
        