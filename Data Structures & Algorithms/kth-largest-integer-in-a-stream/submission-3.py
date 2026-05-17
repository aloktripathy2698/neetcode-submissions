from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        
        for num in nums:
            self.__insert(num)

    def __insert(self, val):
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        self.__insert(val)
        return self.min_heap[0]
        
