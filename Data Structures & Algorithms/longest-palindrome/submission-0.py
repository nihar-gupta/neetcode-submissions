class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for i in s: d[i] = d.get(i, 0) + 1
        c = 0
        odd = True
        for i in d.values():
            if i&1 != 0: 
                if odd:
                    c+=i
                    odd=False
                else:
                    c += (i-1)
            else:
                c += i
        return c