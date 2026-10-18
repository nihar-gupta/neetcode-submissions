class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def xor_of_n(n):
            rem = n%4
            if rem == 0: return n
            elif rem == 1: return 1
            elif rem == 2: return n+1
            else: return 0
        
        n = len(nums)
        xor = xor_of_n(n)
        for i in nums: xor = xor^i
        return xor
        