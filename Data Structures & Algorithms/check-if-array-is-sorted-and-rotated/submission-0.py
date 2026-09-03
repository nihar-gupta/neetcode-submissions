class Solution:
    def check(self, nums: List[int]) -> bool:
        c =  0
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                c += 1
        if c>1: return False 
        if c==0: return True 
        if nums[0] < nums[-1]: return False
        return True

        
        