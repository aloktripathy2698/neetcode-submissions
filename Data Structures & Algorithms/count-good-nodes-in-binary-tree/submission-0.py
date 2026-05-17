# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, maxVal):
        if not node:
            return
        if node.val >= maxVal:
            self.count += 1
            maxVal = node.val
        self.dfs(node.left, maxVal)
        self.dfs(node.right, maxVal)        

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count += 1
        self.dfs(root.left, root.val)
        self.dfs(root.right, root.val)
        return self.count

        
        