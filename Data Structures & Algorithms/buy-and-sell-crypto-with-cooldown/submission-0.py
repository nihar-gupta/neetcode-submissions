class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(prices, i, buy, cool):
            if i == len(prices): return 0

            bb = 1 if buy else 0
            cc = 1 if cool else 0

            if i in d and bb in d[i] and cc in d[i][bb]:
                return d[i][bb][cc]

            if buy:
                if cool:
                    ans = solve(prices, i+1, buy, False)
                    #return p1
                else:
                    p1 = solve(prices, i+1, buy, False)
                    p2 = -prices[i] + solve(prices, i+1, False, True)
                    ans= max(p1, p2)
            else:
                p1 = solve(prices, i+1, False, True)
                p2 = prices[i] + solve(prices, i+1, True, True)
                ans = max(p1,p2)
            if i not in d:
                d[i] = dict()
            if bb not in d[i]:
                d[i][bb] = dict()
            if cc not in d[i][bb]:
                d[i][bb][cc] = 0
            d[i][bb][cc] = ans
            return ans
        d = dict()
        return solve(prices, 0, True, False)

        