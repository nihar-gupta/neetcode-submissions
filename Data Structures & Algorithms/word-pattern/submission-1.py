class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d =dict()
        s=s.split()
        if len(pattern) != len(s): return False
        n = len(pattern)
        dd = dict()
        for i in range(n):
            if pattern[i] in d and d[pattern[i]] != s[i]: return False
            if s[i] in dd and dd[s[i]] != pattern[i]: return False
            d[pattern[i]] = s[i]
            dd[s[i]] = pattern[i]
        return True

        