from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapify(max_heap)

        time = 0
        while max_heap:
            curr_time = 0
            pending = deque()
            while max_heap and curr_time <= n:
                freq = -heappop(max_heap)
                freq -= 1
                if freq:
                    pending.append(freq)
                curr_time += 1

            while pending:
                heappush(max_heap, -pending.popleft())

            if not max_heap:
                time += curr_time
            else:
                time += n + 1

        return time



