class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = True
        c = 1
        mc = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if inc == True:
                    c += 1
                    mc = max(mc, c)
                else:
                    inc = True
                    c = 2
                    mc = max(mc,c)
            elif nums[i] < nums[i-1]:
                if inc == False:
                    c += 1
                    mc = max(mc, c)
                else:
                    inc = False
                    c = 2
                    mc = max(mc, c)
            else:
                c = 1
        return mc

                
        