class Solution:
    def canJump(self, a: List[int]) -> bool:

        min_range = 0
        max_range = 0

        n = len(a)
        
        while max_range < n-1:
            if min_range > max_range: return False
            farthest = min_range

            for i in range(min_range, max_range+1):
                farthest = max(farthest, i+a[i])
            
            min_range = max_range+1
            max_range = farthest
        
        return max_range>=n-1



        