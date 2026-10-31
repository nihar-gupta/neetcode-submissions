import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        heap = []

        for trip in trips:
            heapq.heappush(heap, [trip[1], trip[2], trip[0]])
        
        current = 0
        out = []

        while len(heap) > 0:
            

            if len(out) > 0 and out[0][0] <= heap[0][0]:
                curr = heapq.heappop(out)
                current -= curr[1]
            else:
                curr = heapq.heappop(heap)
                current += curr[2]
                if current > capacity: return False 
                heapq.heappush(out, [curr[1], curr[2]])
        return True



        