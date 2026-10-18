class Solution:
    def reverse(self, x: int) -> int:
        def rev(s):
            rt = ""
            for i in range(len(s)-1,-1,-1):
                rt += s[i]
            return rt

        sign = False
        if x < 0:
            sign = True 
            x = abs(x)

        s = str(x)
        ss = rev(s)
        ss = int(ss)
        if sign:
            ss = -ss

        if ss > (1<<31)-1: return 0
        elif ss < -(1<<31)-1: return 0
        return ss
            