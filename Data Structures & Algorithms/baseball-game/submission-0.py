class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0

        for i in operations:
            if i == "+":
                p1 = stack[-1]
                p2 = stack[-2]
                c = p1+p2
                stack.append(c)
                ans+=c 
            elif i == "C":
                p1 = stack[-1]
                stack.pop()
                ans -= p1
            elif i == "D":
                p1 = stack[-1]
                stack.append(2*p1)
                ans += 2*p1
            else:
                stack.append(int(i))
                ans += int(i)
        return ans
        