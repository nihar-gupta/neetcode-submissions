class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        def pc(n):
            return n*(n+1)//2
        
        d = dict()
        for i in a: d[i]=d.get(i, 0)+1
        ans = 0
        for i in d.values():
            if i>1:
                ans += pc(i-1)
        return ans

        