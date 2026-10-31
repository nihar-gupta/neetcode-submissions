import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        d = dict()
        for i in s: d[i] = d.get(i, 0) + 1

        rt = ""
        for key, val in d.items():
            heapq.heappush(heap, [-val, ord(key)])
        
        while len(heap) > 0:
            k1 = heapq.heappop(heap)
            k2 = None
            if len(heap) > 0:
                k2 = heapq.heappop(heap)
            
            if k2 is None and -k1[0]>1: return ""

            # if len(rt) > 0 and rt[-1] == chr(k1[1]):
            #     if k2 == None: return ""
            #     k1, k2= k2, k1



            rt += chr(k1[1])
            if -k1[0] > 1:
                heapq.heappush(heap, [k1[0]+1, k1[1]])
            
            if k2 is not None:
                rt += chr(k2[1])
                if -k2[0] > 1:
                    heapq.heappush(heap, [k2[0]+1, k2[1]])
        return rt

        