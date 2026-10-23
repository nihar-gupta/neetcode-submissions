class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:

        stack = []
        rt = []

        for i in range(len(t)-1,-1,-1):

            while len(stack) > 0 and t[stack[-1]] <= t[i]:
                stack.pop()
            
            if len(stack) == 0:
                rt.append(0)
            else:
                rt.append(stack[-1] - i)
            
            stack.append(i)
        return rt[::-1]

        