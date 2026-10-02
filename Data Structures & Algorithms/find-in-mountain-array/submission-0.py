class Solution:

    def f(self, m, key):
        if key in self.got:
            return self.got[key]
        val = m.get(key)
        self.got[key] = val
        return val

    def findInMountainArray(self, target: int, m: 'MountainArray') -> int:

        self.got = dict()

        n = m.length()

        low = 1
        high = n-2

        while low<=high:
            mid = (low+high)//2
            mid_ele = self.f(m, mid)

            m1_ele = self.f(m, mid-1)
            m2_ele = self.f(m, mid+1)
            
            if m1_ele < mid_ele and mid_ele > m2_ele:
                found = True
                mount_index = mid
                mount_ele = mid_ele
                break
            
            if m1_ele > mid_ele and mid_ele > m2_ele:
                high = mid-1
            else:
                low = mid+1
        

        low = 0
        high = mount_index
        ans = None
        while low<=high:
            mid = (low+high)//2

            mid_ele = self.f(m, mid)
            if mid_ele == target:
                ans = mid 
                high = mid - 1
            elif mid_ele > target:
                high = mid - 1
            else:
                low = mid+1
        
        if ans != None: return ans 
    
        low = mount_index
        high = n - 1
        ans = None
        while low <= high:
            mid = (low+high)//2

            mid_ele = self.f(m, mid)
            if mid_ele == target:
                ans = mid 
                return mid 
            elif mid_ele > target:
                low = mid+1
            else:
                high = mid-1
        return -1





