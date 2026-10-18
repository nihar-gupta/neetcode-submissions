class Solution:
    def addBinary(self, a: str, b: str) -> str:
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



        