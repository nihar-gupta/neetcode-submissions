class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        i = 1
        c = 1
        while i<n:
            if nums[i] != nums[i-1]:
                j+=1
                nums[j] = nums[i]
                c+=1
            i+=1
        return c
        