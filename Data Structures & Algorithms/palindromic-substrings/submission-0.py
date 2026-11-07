class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)
        for i in range(n):

            p1 = i
            p2 = i
            while p1 >= 0 and p2 < n and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
                c+=1
            
            p1 = i
            p2 = i+1
            while p1 >= 0 and p2 < n and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
                c+=1
        return c

        