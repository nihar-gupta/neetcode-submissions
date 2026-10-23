class Solution:
    def decodeString(self, s: str) -> str:

        number = []
        for i in range(10):
            number.append(str(i))

        
        stack = []
        for i in s:
            if i == "]":
                temp = []
                while len(stack) > 0 and stack[-1] != "[":
                    temp.append(stack[-1])
                    stack.pop()
                
                temp.reverse()
                temp = "".join(temp)
                stack.pop()
                nn = int(stack.pop())
                temp = nn*temp
                stack.append(temp)
            else:
                if i in number and len(stack) > 0 and stack[-1][-1] in number :
                    stack[-1] = stack[-1] + i
                else:
                    stack.append(i)
        rt = ""
        for i in stack:
            rt+=i
        return rt


        