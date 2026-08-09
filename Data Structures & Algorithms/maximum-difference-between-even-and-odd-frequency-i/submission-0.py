class Solution:
    def maxDifference(self, s: str) -> int:
        d = dict()
        for i in s: d[i] = d.get(i, 0)+1
        odd_freq = 0
        even_freq = 10000
        for i,j in d.items():
            if j%2 == 0:
                even_freq = min(even_freq, j)
            else:
                odd_freq = max(odd_freq, j)
        return odd_freq - even_freq

        