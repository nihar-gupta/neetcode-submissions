class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d =dict()
        for i in arr: d[i] = d.get(i, 0)+1
        mc = -1
        for i,j in d.items():
            if i==j:
                mc=max(mc, i)
        return mc if mc > 0 else -1
        