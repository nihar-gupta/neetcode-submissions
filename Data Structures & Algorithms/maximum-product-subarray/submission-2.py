class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        p = 1
        rt = float('-inf')
        n = len(nums)
        for i in range(n):
            p = p*nums[i]
            rt = max(rt, p)
            if p == 0:
                p = 1
        
        p = 1
        for i in range(n-1, -1, -1):
            p = p*nums[i]
            rt = max(rt, p)
            if p == 0:
                p = 1

        return rt
