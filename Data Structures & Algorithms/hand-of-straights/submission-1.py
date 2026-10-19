class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        def findmin(a):
            return min(a)
        d = dict()
        for i in hand:
            d[i] = d.get(i, 0)+1
        
        while len(d) != 0:
            p = findmin(d.keys())
            d[p] -= 1
            if d[p] == 0:
                d.pop(p)
            for i in range(p+1, p+groupSize):
                if i not in d: return False
                d[i] -= 1
                if d[i] == 0: d.pop(i)
        return True

        