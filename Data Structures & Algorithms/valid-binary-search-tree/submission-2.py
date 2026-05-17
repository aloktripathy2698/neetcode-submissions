# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left_min, right_max):
            if not node:
                return True
            if not left_min < node.val < right_max:
                return False
            return dfs(node.left, left_min, node.val) and dfs(node.right, node.val, right_max)


        return dfs(root, float("-inf"), float("inf"))
        