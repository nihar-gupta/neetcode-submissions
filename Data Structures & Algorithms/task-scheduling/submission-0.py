import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        d = dict()
        for i in tasks: d[i] = d.get(i, 0) + 1
        for key, val in d.items(): heapq.heappush(heap, -val)

        ans = 0
        while len(heap) > 0:
            window = n+1
            used = 0
            insert = []
            while len(heap) > 0 and used < window:
                curr = -heapq.heappop(heap)
                used+=1
                if curr-1 > 0:
                    insert.append(curr-1)
            if used == window:
                ans += used 
            elif len(heap) == 0:
                if len(insert) == 0:
                    ans += used 
                else:
                    ans += window
            for ii in insert:
                heapq.heappush(heap, -ii)
        return ans
            



        