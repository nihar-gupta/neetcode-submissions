class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        q = 0
        for i in nums:
            if i != 0:
                p=p*i
            if i==0: q+=1
        if q == len(nums): return [0 for i in range(q)]
        rt = []
        for i in nums:
            if i == 0:
                if q>1: rt.append(0)
                else: rt.append(p)
            else:
                if q>0: rt.append(0)
                else: rt.append(p//i)
        return rt
        