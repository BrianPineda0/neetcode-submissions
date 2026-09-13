class MedianFinder:

    def __init__(self):

        self.minHeap = [] # will have all the n/2 min values and will be negative so we can get the greatest min val
        self.maxHeap = [] # will have all the n/2 mac values and will be positive so we can get the smallest max val

    def addNum(self, num: int) -> None:

        heapq.heappush(self.minHeap, -num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.maxHeap) > len(self.minHeap):                      # This balances the heap makes it so they are either equal
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap)) # or off by one where the minHeap would have the median at 
                                                                       # the top 

    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):                       # Since we made it so the top of the small heap has the 
                                                                        # median value then we will pop from it
            return -self.minHeap[0]
        return (-self.minHeap[0] + self.maxHeap[0])/2

        
        
        