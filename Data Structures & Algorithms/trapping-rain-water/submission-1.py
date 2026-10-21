class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        ans = 0
        left_max = 0
        right_max = 0

        p1 = 0
        p2 = n-1

        while p1<p2:

            if height[p1] <= height[p2]:
                # then for sure we have a taller building on the right
                # atleast p2 building is taller 

                # so to store the water we need a building on the left 
                # which is taller than the current one 
                # so left_max will give us those details 

                if left_max > height[p1]:
                    ans += left_max - height[p1]
                else:
                    left_max = height[p1]
                p1 += 1

                # here you may ask why did we only considered left max 
                # meaning we are directly stating that 
                # left max is min compared with right max 
                # because if the rigth side is lesser then we would have 
                # traversed it first (ie. p2-=1)
            else:

                if right_max > height[p2]:
                    ans += right_max - height[p2]
                else:
                    right_max = height[p2]
                
                p2-=1
        return ans












                # right_max = []
                
                # r_max = 0
                # for i in height:
                #     right_max.append(r_max)
                #     r_max = max(r_max, i)
                
                # left_max = []
                # l_max = 0
                # n = len(height)
                # for i in range(n-1, -1, -1):
                #     left_max.append(l_max)
                #     l_max = max(l_max, height[i])
                
                # left_max = left_max[::-1]

                # ans = 0
                # for i in range(1, n-1):
                #     if left_max[i] > height[i] and height[i] < right_max[i]:
                #         ans += min(left_max[i], right_max[i]) - height[i]
                # return ans
                