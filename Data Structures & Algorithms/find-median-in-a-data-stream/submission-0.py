# class MedianFinder:

#     def __init__(self):
        

#     def addNum(self, num: int) -> None:
        

#     def findMedian(self) -> float:
        
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num):
        
        # push elements into small with -num because we need to get the maximum of small at any moment 
        # push elements into large with num because we need to get min of large at any moment

        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # small can have atmax 1 more element compared with large 
        # but larget cannot have more elements at any moment
        if len(self.small) - len(self.large) > 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val) 
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0] )/2