class Solution:
    def splitArray(self, a: List[int], k: int) -> int:
        def f1(a):
            ma = a[0]
            su = 0
            for i in a:
                ma = max(ma, i)
                su += i
            return ma, su
        
        def solve(a, su, k):
            kk = 1
            s = 0
            i = 0
            while i<len(a):
                if s + a[i] > su:
                    kk += 1
                    s = a[i]
                else:
                    s += a[i]
                
                if kk > k: return False
                
                i+=1
            
            if kk > k: return False
            return True
        
        low, high = f1(a)
        ans = None
        while low<=high:
            mid = (low+high)//2

            if solve(a, mid, k):
                ans = mid
                high = mid - 1
            else:
                low = mid+1
        
        return ans
        