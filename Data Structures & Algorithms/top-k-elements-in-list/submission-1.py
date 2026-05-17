class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap,(count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for _, num in heap:
            ans.append(num)
        return ans
        