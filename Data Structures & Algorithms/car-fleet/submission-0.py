class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        def ms(a, b):
            if len(a) <= 1:
                return a,b
            
            n = len(a)
            m = n//2

            a1, b1 = ms(a[:m], b[:m])
            a2, b2 = ms(a[m:], b[m:])

            a, b = merge(a1,b1,a2,b2)
            return a, b
        
        def merge(a1, b1, a2, b2):
            a = []
            b = []

            p1 = 0
            p2 = 0
            n = len(a1)
            m = len(a2)
            while p1<n and p2<m:
                if a1[p1] < a2[p2]:
                    a.append(a1[p1])
                    b.append(b1[p1])
                    p1+=1
                else:
                    a.append(a2[p2])
                    b.append(b2[p2])
                    p2+=1
            while p1<n:
                a.append(a1[p1])
                b.append(b1[p1])
                p1+=1
            while p2<m:
                a.append(a2[p2])
                b.append(b2[p2])
                p2+=1
            return a,b


        position, speed = ms(position, speed)
        stack = []
        n = len(position)

        for i in range(n-1, -1, -1):
            time = (target-position[i])/speed[i]

            if len(stack) > 0 and stack[-1] >= time:
                pass
            else:
                stack.append(time)
            
        return len(stack)
        