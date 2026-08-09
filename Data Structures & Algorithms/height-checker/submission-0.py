class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=0
        h = heights.copy()
        h.sort()
        for i in range(len(heights)):
            if heights[i] != h[i]: c+=1
        return c
        