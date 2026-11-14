class Solution:
    def lastStoneWeightII(self, a: List[int]) -> int:
        def solve(a, i, cs, s):
            if i == len(a):
                ans = abs(cs-(s-cs))
                return ans
            
            if i in d and cs in d[i]: return d[i][cs]
            
            a1 = solve(a, i+1, cs+a[i], s)
            a2 = solve(a, i+1, cs, s)

            if i not in d:
                d[i] =dict()
            if cs not in d:
                d[i][cs] = 0
            d[i][cs] = min(a1, a2)
            return min(a1, a2)

        d = dict()
        s = sum(a)
        return solve(a, 0, 0, s)
        

        
        