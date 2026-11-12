class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(a, b, i, j):
            if i == len(a) or j == len(b): return 0

            if i in d and j in d[i]: return d[i][j]
            if a[i] == b[j]:
                p = 1 + solve(a, b, i+1, j+1)
            else:
                p = max(solve(a, b, i+1, j), solve(a, b, i, j+1))
            
            if i not in d:
                d[i] = dict()
            d[i][j] = p
            return p

        d = dict()
        return solve(text1, text2, 0, 0)
        