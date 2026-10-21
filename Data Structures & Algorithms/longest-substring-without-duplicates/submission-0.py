class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        ans = 0
        j = 0
        n = len(s)
        for i in range(n):
            if s[i] not in d:
                d.add(s[i])
                ans = max(ans, len(d))
            else:
                while s[i] in d:
                    d.remove(s[j])
                    j+=1
                d.add(s[i])
                ans = max(ans, len(d))
        return ans
            

        