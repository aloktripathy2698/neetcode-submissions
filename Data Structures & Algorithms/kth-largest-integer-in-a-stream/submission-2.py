from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.size = k
        for num in nums:
            heappush(self.min_heap, num)
            self.maintain_size()

    def maintain_size(self):
        if len(self.min_heap) > self.size:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        self.maintain_size()
        return self.min_heap[0]

        
