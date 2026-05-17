# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return 0, True
        left, isBalancedLeft = self.dfs(root.left)
        right, isBalancedRight = self.dfs(root.right)
        isBalanced = isBalancedLeft and isBalancedRight and abs(left - right) <= 1
        return 1 + max(left, right), isBalanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
        