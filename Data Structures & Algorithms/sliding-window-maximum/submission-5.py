class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # [0, 1, ]
        res = []
        for i in range(len(nums)):# i = 0, nums[0] = 1
            while q and i - k >= q[0]:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

        