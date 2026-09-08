class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minHeap = []

        for val in nums:
            heapq.heappush(minHeap, val)

            if k < len(minHeap):
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)