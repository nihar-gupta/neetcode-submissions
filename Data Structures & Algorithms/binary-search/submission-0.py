class Solution:
    def search(self, a: List[int], target: int) -> int:
        low = 0
        high = len(a)-1
        while low<=high:
            mid = (low+high)//2
            if a[mid] == target: return mid 
            elif a[mid] > target: high = mid - 1
            else: low = mid + 1
        return -1

        