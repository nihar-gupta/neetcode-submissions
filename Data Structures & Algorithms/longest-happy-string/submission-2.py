import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []

        if a>0:
            heapq.heappush(heap, [-a, ord("a")])
        if b>0:
            heapq.heappush(heap, [-b, ord("b")])
        if c>0:
            heapq.heappush(heap, [-c, ord("c")])
        
        rt = ""

        while len(heap) > 0:
            p1 = heapq.heappop(heap)

            if len(rt) == 0 or (len(rt) > 0 and rt[-1] != chr(p1[1])):
                if -p1[0] >= 2:
                    rt += chr(p1[1]) + chr(p1[1])
                    p1[0]+=2
                else:
                    rt += chr(p1[1])
                    p1[0] += 1

                if -p1[0] > 0:
                    heapq.heappush(heap, p1)
            else:
                if len(rt) <= 1 or (rt[-2] != chr(p1[1])):
                    rt += chr(p1[1])
                    p1[0] += 1
                    heapq.heappush(heap, p1)
                    continue

                if len(heap) > 0:
                    p2 = heapq.heappop(heap)
                    rt += chr(p2[1])
                    p2[0] += 1

                    if -p2[0] > 0:
                        heapq.heappush(heap, p2)
                    
                    heapq.heappush(heap, p1)
                    continue
                
                return rt
        return rt



            




        