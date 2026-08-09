class Solution:
    def maxAscendingSum(self, a: List[int]) -> int:
        
        mc = a[0]
        c = a[0]
        n = len(a)
        for i in range(1, n):
            if a[i] > a[i-1]:
                c = c + a[i]
            else:
                c = a[i]
            mc = max(mc, c)
        return mc
