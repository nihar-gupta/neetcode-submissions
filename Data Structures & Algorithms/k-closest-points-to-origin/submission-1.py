import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            val = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap,[val, point[0], point[1]])
        
        rt = []
        while len(rt) < k and len(heap) > 0:
            curr = heapq.heappop(heap)
            rt.append([curr[1],curr[2]])
        return rt

        