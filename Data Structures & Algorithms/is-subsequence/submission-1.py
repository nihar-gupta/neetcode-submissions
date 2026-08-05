class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        got_all = False
        n = len(s)
        m = len(t)

        i=0
        j=0
        while j<m and i<n:
            if t[j] == s[i]:
                i+=1
            j+=1
        if i>=n: return True 
        return False
                


        