class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        min_index = 0
        max_index = 0

        n = len(nums)

        while max_index < n-1:
            far = float('-inf')

            for i in range(min_index, max_index+1):
                far = max(far, i+nums[i])
            
            min_index = max_index+1
            max_index = far
            jump+=1
        return jump
        