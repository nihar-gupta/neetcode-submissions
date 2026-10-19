class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        c = 0
        i = 0
        n = len(nums)
        while i<n:
            c = c+nums[i]
            ans = max(ans, c)
            if c<0:
                c=0
            i+=1
        return ans
        