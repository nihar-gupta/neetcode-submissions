class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxi = 0
        ans = None 

        for i in range(n):
            
            j1 = i
            j2 = i
            
            while j1>=0 and j2<n and s[j1] == s[j2]:
                if j2 - j1 + 1 > maxi:
                    maxi = j2 - j1 + 1
                    ans = s[j1:j2+1]
                j1 -= 1
                j2 += 1
            
            j1 = i
            j2 = i + 1
            
            while j1>=0 and j2<n and s[j1] == s[j2]:
                if j2 - j1 + 1 > maxi:
                    maxi = j2 - j1 + 1
                    ans = s[j1:j2+1]
                j1 -= 1
                j2 += 1
        return ans
                