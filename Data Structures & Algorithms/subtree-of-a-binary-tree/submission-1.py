# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            return sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)

        def singleDfs(node):
            if not node and not subRoot:
                return True
            if not node:
                return False
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    return True
            return singleDfs(node.left) or singleDfs(node.right)

        return singleDfs(root)
            


        

            
        