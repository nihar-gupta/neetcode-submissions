class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

# class Solution:
#     def largestRectangleArea(self, heights):

        n = len(heights)

        left_min = []
        stack = []

        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if len(stack) == 0:
                left_min.append(-1)
            else:
                left_min.append(stack[-1])
            
            stack.append(i)


        right_min = []
        stack = []

        for i in range(n-1,-1,-1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if len(stack) == 0:
                right_min.append(n)
            else:
                right_min.append(stack[-1])
            
            stack.append(i)
        
        right_min.reverse()

        #print(left_min)
        #print(right_min)

        ans = 0
        for i in range(n):
            #if left_min[i] != -1 and right_min[i] != -1:
            blocks = (right_min[i] - 1) - (left_min[i] +1) +1
            ans = max(ans, blocks*heights[i])
        return ans
        


      