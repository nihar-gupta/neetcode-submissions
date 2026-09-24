class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1 = None 
        c1 = 0
        e2 = None 
        c2 = 0

        for i in nums:
            if i==e1:
                c1+=1
            elif i==e2:
                c2+=1
            else:
                if c1 == 0:
                    e1 = i
                    c1 = 1
                elif c2 == 0:
                    e2 = i
                    c2 = 1
                else:
                    c1 -= 1
                    c2 -= 1
        
        c1 = 0
        c2 = 0
        for i in nums:
            if i == e1: c1+=1
            elif i == e2: c2+=1
        
        n= len(nums)//3
        rt = []
        if c1>n: rt.append(e1)
        if c2>n: rt.append(e2)
        return rt

        
