class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        o = 0
        t = 0
        for i in nums: 
            if i==0: z+=1
            elif i==1: o+=1
            else: t+=1
        i=0
        while i<z:
            nums[i] = 0
            i+=1
        j=0
        while j<o:
            nums[i] = 1
            i+=1
            j+=1
        
        j=0
        while j<t:
            nums[i] = 2
            i+=1
            j+=1
        return nums
        