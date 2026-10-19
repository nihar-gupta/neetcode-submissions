class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:        
        ans = float('-inf')
        i=0
        n=len(a)
        c=0
        while i<n:
            c+=a[i]
            ans = max(ans, c)
            if c<0: c=0
            i+=1
        
        ltr = []
        c=0
        mc = float('-inf')
        for i in range(n):
            c=c+a[i]
            mc =max(mc, c)
            ltr.append(mc)
        
        rtl = []
        c=0
        mc = float('-inf')
        for i in range(n-1,-1,-1):
            c=c+a[i]
            mc =max(mc, c)
            rtl.append(mc)
        
        rtl=rtl[::-1]

        for i in range(n-1):
            ans = max(ans, ltr[i] + rtl[i+1])
        return ans



