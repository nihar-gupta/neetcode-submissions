import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        heap = []
        rt = []

        n = len(tasks)
        for i in range(n):
            heapq.heappush(heap, [tasks[i][0], tasks[i][1], i])
        

        time = 0
        while len(heap) > 0:
            if time < heap[0][0]:
                time = heap[0][0]
            
            items = []

            while len(heap) > 0 and heap[0][0] <= time:
                curr = heapq.heappop(heap)
                heapq.heappush(items, [curr[1], curr[2]])
            
            while len(items) > 0:
                curr = heapq.heappop(items)
                rt.append(curr[1])
                time = time + curr[0]

                while len(heap) > 0 and heap[0][0] <= time:
                    curr = heapq.heappop(heap)
                    heapq.heappush(items, [curr[1], curr[2]])
            
        return rt
        
            


        
        
        
        
        