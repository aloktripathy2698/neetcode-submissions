class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i in range(len(nums)):
            if q and i >= k:
                ans.append(nums[q[0]])
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if q and i - k >= q[0]:
                q.popleft()
        ans.append(nums[q[0]])
        return ans