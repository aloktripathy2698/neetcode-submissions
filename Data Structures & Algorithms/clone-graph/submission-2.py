"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        mp = {}

        def dfs(node):
            if node in mp:
                return mp[node]
            
            mp[node] = Node(node.val)
            for child in node.neighbors:
                mp[node].neighbors.append(dfs(child))
            return mp[node]

        return dfs(node)
        