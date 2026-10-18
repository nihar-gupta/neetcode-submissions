class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def binary(n):
            s= []
            while n>0:
                bit = n&1
                s.append(bit)
                n=n>>1

            return s

        bx = binary(x)
        bn = binary(n-1)
        
        j=0
        len_of_bx = len(bx)
        for i in bn:

            found = False
            while j<len_of_bx:
                if bx[j] == 0:
                    bx[j] = i
                    j+=1
                    found = True
                    break
                else:
                    j+=1
            
            if not found:
                bx.append(i)

        print(bx)
        ans = 0
        bit = 0
        for i in bx:
            if i == 1:
                ans = ans | (1<<bit)
            bit +=1
        return ans

    
            
