from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            x, y = heappop(max_heap), heappop(max_heap)
            z = -abs(abs(x) - abs(y))
            if z != 0:
                heappush(max_heap, z)
        
        return -max_heap[0] if max_heap else 0
        