class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

# class Solution:
#     def asteroidCollision(self, asteroids):
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:

                current_exist = True

                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < -i:
                    stack.pop()

                if len(stack) > 0 and stack[-1] < 0:
                    stack.append(i)
                    continue


                if len(stack) > 0 and stack[-1] == -i:
                    stack.pop()
                    current_exist = False
                
                elif len(stack) > 0 and stack[-1] > -i:
                    current_exist = False
                
                if current_exist:
                    stack.append(i)
        return stack
                
  