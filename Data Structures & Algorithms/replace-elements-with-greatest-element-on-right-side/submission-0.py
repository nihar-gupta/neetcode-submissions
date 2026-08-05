class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        maxi = 0
        n=len(a)
        for i in range(n-1,-1,-1):
            if i==n-1: 
                maxi = a[i]
                a[i] = -1
            else:
                pre_max = maxi
                maxi =max(a[i], maxi)
                a[i] = pre_max
                
        return a
        