class Solution:
    def isMonotonic(self, a: List[int]) -> bool:
        if len(a)<=1: return True 
        inc = 1 if a[0]<=a[1] else 0
        if inc:
            for i in range(1, len(a)):
                if a[i-1]>a[i]: return False
            return True
        else:
            for i in range(1, len(a)):
                if a[i-1]<a[i]: return False
            return True
        