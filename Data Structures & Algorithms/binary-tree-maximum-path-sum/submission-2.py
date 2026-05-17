# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -math.inf

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            leftSum = max(0,dfs(node.left))
            rightSum = max(0, dfs(node.right))
            currSum = node.val + leftSum + rightSum
            maxSum = max(maxSum, currSum)
            return node.val + max(leftSum, rightSum)
        
        dfs(root)
        return maxSum

        