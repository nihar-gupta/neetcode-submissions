class Solution:
    def coinChange(self, a: List[int], target: int) -> int:
        def solve(a, target):
            nonlocal d
            if target < 0: rt = float('inf')
            elif target == 0: rt = 0
            else:
                if target in d: return d[target]
                mini = float('inf')
                n = len(a)
                for i in range(n):
                    mini = min(mini, solve(a, target-a[i]))
                
                rt = 1+mini
            if target not in d:
                d[target] = 0
            d[target] = rt
            return rt
        
        d = dict()
        mini = solve(a, target)
        if mini == float('inf'): return -1
        return mini
