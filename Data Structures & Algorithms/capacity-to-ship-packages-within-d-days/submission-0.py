class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def solve(a, w, d):
            days = 1
            s = 0
            i = 0 
            while i<len(a):
                if a[i] + s > w:
                    days +=1
                    s = 0
                else:
                    s = s + a[i]
                    i+=1
                if days > d: return False
            
            return days<=d
        
        def solve2(a):
            ma = a[0]
            su = 0
            for i in a:
                ma = max(i, ma)
                su += i
            return ma, su



        low, high = solve2(weights)
        ans = high
        while low<=high:
            mid = (low+high)//2

            if solve(weights, mid, days):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
        