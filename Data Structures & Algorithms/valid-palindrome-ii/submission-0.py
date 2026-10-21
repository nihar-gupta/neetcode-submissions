class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(a, k):
            i = 0
            j = len(a)-1
            while i<j:
                if k==i:
                    i+=1
                elif k==j:
                    j-=1
                
                if i>=j: return True 

                if s[i] != s[j]: return False
                i+=1
                j-=1
            return True
        
        n = len(s)
        for i in range(n):
            if check(s, i):
                return True
        return False



        