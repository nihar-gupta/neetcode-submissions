class Solution:
    def minEatingSpeed(self, a: List[int], h: int) -> int:
        def solve(a, k, h):
            hour = 0
            for i in a:
                if i < k:
                    hour +=1
                else:
                    if i%k == 0:
                        hour += i//k
                    else:
                        hour += (i//k + 1)
                if hour > h: return False
            if hour <= h: return True
            return False

        low = 1
        high = max(a)
        ans = None
        while low<=high:
            mid = (low+high)//2

            if solve(a, mid, h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        