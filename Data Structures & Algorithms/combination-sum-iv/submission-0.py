class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def solve(a, target):
            if target == 0: return 1
            
            if target in d: return d[target]
            p = 0
            for i in range(len(a)):
                if target-a[i] >= 0:
                    p += solve(a, target-a[i])
            d[target] = p
            return p

        d = dict()
        return solve(nums, target)