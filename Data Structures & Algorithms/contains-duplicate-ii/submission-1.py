class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = dict()
        i = 0
        j = 0
        n = len(nums)
        c = 0
        while i<n:
            if c <= k:
                if nums[i] in d:
                    return True
                else:
                    d[nums[i]] = 1
                    c+=1
            else:
                while c >= k and j<i:
                    d.pop(nums[j])
                    c-=1
                    j+=1
                if nums[i] in d:
                    return True
                else:
                    d[nums[i]] = 1
                    c+=1
            i+=1
        return False
        