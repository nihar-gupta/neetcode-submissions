class Solution:
    def countBits(self, n: int) -> List[int]:
        def bits(n):
            c=0
            while n>0: 
                n=n&(n-1)
                c+=1
            return c
        
        rt = []
        for i in range(n+1):
            rt.append(bits(i))
        
        return rt
        