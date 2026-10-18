class Solution:
    def getSum(self, a: int, b: int) -> int:
        def addBinary(a: str, b: str) -> str:
            def reverse(s):
                p = ""
                for i in range(len(s)-1,-1,-1):
                    p+=s[i]
                return p

            rt = ""
            v = 0

            i = len(a)-1
            j = len(b)-1
            carry = 0
            while i>=0 and j>=0:
                kk = int(a[i]) + int(b[j]) + carry 
                if kk == 0:
                    carry = 0
                    rt += "0"
                elif kk == 1:
                    carry = 0
                    rt += "1"
                elif kk == 2:
                    carry = 1
                    rt += "0"
                elif kk == 3:
                    carry = 1
                    rt += "1"
                v+=1
                i-=1
                j-=1
            
            while i>=0:
                kk = int(a[i]) + carry 
                if kk == 0:
                    carry = 0
                    rt += "0"
                elif kk == 1:
                    carry = 0
                    rt += "1"
                elif kk == 2:
                    carry = 1
                    rt += "0"
                elif kk == 3:
                    carry = 1
                    rt += "1"
                v+=1
                i-=1
            
            while j>=0:
                kk = int(b[j]) + carry 
                if kk == 0:
                    carry = 0
                    rt += "0"
                elif kk == 1:
                    carry = 0
                    rt += "1"
                elif kk == 2:
                    carry = 1
                    rt += "0"
                elif kk == 3:
                    carry = 1
                    rt += "1"
                v+=1
                j-=1
            if carry == 1:
                rt+="1"
            rt = reverse(rt)
            return rt
        def convert(n):
            s=""
            for i in range(31,-1,-1):
                if n&(1<<i) != 0:
                    # set 
                    s=s+"1"
                else:
                    s=s+"0"
            return s
        
        def reverseConvert(s):
            rt = 0
            bit = 0
            for i in range(len(s)-1,-1,-1):
                if s[i] == "1":
                    rt = rt + (1<<bit)
                bit +=1
            return rt
        
        aa = convert(a)
        bb = convert(b)
        pp = addBinary(aa, bb)
        
        # Keep only the lower 32 bits
        pp = pp[-32:]

        pp = reverseConvert(pp)

        # Convert unsigned 32-bit result to signed integer
        if pp >= (1 << 31):
            pp -= (1 << 32)

        return pp
                        

            