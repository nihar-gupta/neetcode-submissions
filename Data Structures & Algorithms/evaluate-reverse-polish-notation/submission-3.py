class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i=="+":
                k1 = stack.pop()
                k2 = stack.pop()
                stack.append(k1+k2)
            elif i=="-":
                k1 = stack.pop()
                k2 = stack.pop()
                stack.append(k2-k1)
            elif i=="*":
                k1 = stack.pop()
                k2 = stack.pop()
                stack.append(k1*k2)
            elif i=="/":
                k1 = stack.pop()
                k2 = stack.pop()
                stack.append(int(float(k2)/k1))
            else:
                stack.append(int(i))
        return stack[-1]
