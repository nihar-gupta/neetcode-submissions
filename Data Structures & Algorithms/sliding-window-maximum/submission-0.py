from collections import deque
class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:

        d = deque()

        rt = []
        n = len(a)
        for i in range(n):

            while len(d) > 0 and d[-1] < a[i]:
                d.pop()

            d.append(a[i])

            if i>k-1:
                if a[i-k] == d[0]:
                    d.popleft()
            
            if i>=k-1:
                rt.append(d[0])
        
        return rt

            

        