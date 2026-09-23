class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        one = 0
        zero = 0
        for i in s:
            if i=="0":
                zero+=1
            else:
                one+=1
        
        c0 = 0
        c1 = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                c0 += 1
            else:
                c1 += 1
            
            ans = max(ans, c0+(one-c1))
        return ans




        