class Solution:
    def maxProfit(self, a: List[int]) -> int:

        buyed = False
        buyed_at = None
        profit = 0

        for i in range(1, len(a)):
            if buyed == False:
                # i need to buy 
                if a[i-1] > a[i]: continue

                buyed_at = a[i-1]
                buyed = True
            else:
                # i need to sell
                if a[i-1]<a[i]: continue

                profit += (a[i-1] - buyed_at)
                buyed = False
        
        if buyed: 
            profit += (a[-1] - buyed_at)

        return profit





        # def fun(a, i, buy, curr):

        #     if i>= len(a): return curr

        #     if buy:
        #         p1 = fun(a, i+1, False, curr - a[i])
        #         p2 = fun(a, i+1, True, curr)
        #         return max(p1,p2)
        #     else:
        #         p1 = fun(a, i+1, True, curr+a[i])
        #         p2 = fun(a, i+1, False, curr)
        #         return max(p1,p2)





        # return fun(prices, 0, True, 0)