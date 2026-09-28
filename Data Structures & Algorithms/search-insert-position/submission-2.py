class Solution:
    def searchInsert(self, a: List[int], target: int) -> int:
        low = 0
        high = len(a)-1
        ans = None
        while low<=high:
            mid = (low+high)//2
            if a[mid] == target: return mid 
            elif a[mid] < target:
                ans = mid
                low = mid+1
            else: high = mid-1
        if ans == None: return 0
        return ans+1

        