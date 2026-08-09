class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        rt = []
        n = len(nums)
        for i in range(1,n+1):
            if i not in s: rt.append(i)
        return rt
        