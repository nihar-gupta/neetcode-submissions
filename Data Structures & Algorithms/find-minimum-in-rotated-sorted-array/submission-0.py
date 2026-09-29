class Solution:
    def findMin(self, a: List[int]) -> int:
        n = len(a)

        low = 0
        high = n-1
        ans = a[0]
        while low<=high:
            mid = (low+high)//2

            if a[low] <= a[mid]:
                # mid lies in array 1
                ans = min(ans, a[low])
                low = mid+1
            else:
                # mid lies in array 2
                ans = min(ans, a[mid])
                high = mid-1
        return ans




        