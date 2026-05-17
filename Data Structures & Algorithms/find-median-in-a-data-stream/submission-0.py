from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def balanceHeaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            num = -1 * heappop(self.maxHeap)
            heappush(self.minHeap, num)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            num = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * num)

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        if self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)
        self.balanceHeaps()
        
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        return 0
        
        