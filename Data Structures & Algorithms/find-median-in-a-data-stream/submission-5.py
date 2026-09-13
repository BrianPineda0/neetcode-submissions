class MedianFinder:

    def __init__(self):

        self.minHeap = [] # will have all the n/2 min values and will be negative so we can get the greatest min val
        self.maxHeap = [] # will have all the n/2 mac values and will be positive so we can get the smallest max val

    def addNum(self, num: int) -> None:

        heapq.heappush(self.minHeap, -num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        return (-self.minHeap[0] + self.maxHeap[0])/2

        
        
        