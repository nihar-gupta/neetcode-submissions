class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        n = len(a)
        m = len(a[0])

        req_row = None 
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if a[mid][0] <= target and target <= a[mid][-1]:
                req_row = mid 
                break
            elif target <= a[mid][0]:
                high = mid - 1
            else:
                low = mid+1

        if req_row == None: return False

        low = 0
        high = m-1
        while low<=high:
            mid = (low+high)//2
            if a[req_row][mid] == target:
                return True
            elif a[req_row][mid] < target:
                low = mid+1
            else: high = mid-1

        return False


