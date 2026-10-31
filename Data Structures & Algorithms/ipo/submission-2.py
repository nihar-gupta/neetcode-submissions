import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        ck = 0
        heap = []
        n = len(profits)
        for i in range(n):
            heapq.heappush(heap, [capital[i], -profits[i]])
        
        insert = []
        while ck<k and len(heap) > 0:
            # if heap[0][0] > w: return w

            # curr = heapq.heappop(heap)
            # insert = []
            # if curr[0] > w: return w



            while len(heap) > 0 and heap[0][0] <= w:
                nex = heapq.heappop(heap)
                
                heapq.heappush(insert, nex[1])
            
            if len(insert) == 0: return w
            cur = heapq.heappop(insert)    
            w = w + (-cur)
            ck+=1
        
        while ck < k and len(insert) > 0:
            cur = heapq.heappop(insert)
            w = w + (-cur)
            ck+=1

        return w
        
        