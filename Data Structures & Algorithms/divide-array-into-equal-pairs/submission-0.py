class Solution:
    def divideArray(self, a: List[int]) -> bool:
        d = dict()
        for i in a:
            d[i] = d.get(i,0)+1
        for i in d.values():
            if i&1 != 0: return False
        return True
        