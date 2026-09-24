class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        d[0] = 1
        c=0
        s=0
        for i in nums:
            s+=i
            req = s-k
            if req in d:
                c+=d[req]

        
            d[s]= d.get(s,0)+1
        return c

        