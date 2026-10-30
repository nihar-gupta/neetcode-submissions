import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        
        while len(heap) > 1:
            c1 = -heapq.heappop(heap)
            c2 = -heapq.heappop(heap)
            p = abs(c1-c2)
            if p>0:
                heapq.heappush(heap, -p)
        if len(heap) == 0: return 0
        return -heap[0]
         