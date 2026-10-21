class Solution:
    def trap(self, height: List[int]) -> int:

        right_max = []
        
        r_max = 0
        for i in height:
            right_max.append(r_max)
            r_max = max(r_max, i)
        
        left_max = []
        l_max = 0
        n = len(height)
        for i in range(n-1, -1, -1):
            left_max.append(l_max)
            l_max = max(l_max, height[i])
        
        left_max = left_max[::-1]

        ans = 0
        for i in range(1, n-1):
            if left_max[i] > height[i] and height[i] < right_max[i]:
                ans += min(left_max[i], right_max[i]) - height[i]
        return ans
        