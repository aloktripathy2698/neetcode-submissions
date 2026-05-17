class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        cache = defaultdict(bool)

        def helper(i, target):
            if target == 0:
                return True
            if i == len(nums):
                return False

            if (i, target) in cache:
                return cache[(i, target)]

            res = helper(i + 1, target)

            if nums[i] <= target:
                res |= helper(i + 1, target - nums[i])

            cache[(i, target)] = res

            return res

        return helper(0, target)

