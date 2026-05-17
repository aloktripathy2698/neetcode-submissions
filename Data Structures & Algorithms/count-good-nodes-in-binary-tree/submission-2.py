# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, prev):
            nonlocal count
            if not node:
                return
            if prev is None or node.val >= prev:
                count += 1
                prev = node.val
            dfs(node.left, prev)
            dfs(node.right, prev)

        dfs(root, None)
        return count
        