class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        d = dict()
        n = len(s)
        for i in range(n):
            if s[i] in d:
                ans = max(ans, i - d[s[i]] - 1)
            else:
                d[s[i]] = i
        return ans
        