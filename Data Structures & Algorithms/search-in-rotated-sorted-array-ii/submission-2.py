class Solution:
    def search(self, a: List[int], target: int) -> bool:
        low = 0
        high = len(a)-1

        while low<=high:
            mid = (low+high)//2

            if a[mid] == target:
                return True
            
            if a[low] == a[mid] and a[mid] == a[high]:
                low +=1
                high -=1
                continue 
            
            if a[low] <= a[mid]:
                if a[low] <= target and target <= a[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if a[mid] <= target and target <= a[high]:
                    low = mid+1
                else:
                    high = mid - 1
        return False
        
        