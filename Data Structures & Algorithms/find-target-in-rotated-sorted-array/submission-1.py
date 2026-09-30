class Solution:
    def search(self, a: List[int], target: int) -> int:
        
        low = 0
        high = len(a)-1
        while low<=high:
            mid = (low+high)//2

            if target == a[mid]:
                return mid

            if a[low] == a[mid] and a[mid] == a[high]:
                low+=1
                high-=1
                continue
                
            if a[low] <= a[mid]:
                # mid lies in array 1 
                if a[low] <= target and target <= a[mid]:
                    high = mid - 1
                else:
                    low = mid+1
            else:
                # mid lies in array 2 
                if target >= a[mid] and target <= a[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1 