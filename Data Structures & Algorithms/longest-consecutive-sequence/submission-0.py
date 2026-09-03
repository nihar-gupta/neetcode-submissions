class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums: s.add(i)
        mrt = 0
        for i in nums:
            if i-1 not in s: 
                c = 1
                j = i+1
                while j in s:
                    c+=1
                    j+=1
                mrt = max(mrt, c)
        return mrt
        