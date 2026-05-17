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
            return None

        mp = {} # {1: [1, [2]], 2: [2, [1, 3]], 3: [3, []]}

        def dfs(node): # 1 | 2
            if node in mp:
                return mp[node]
            mp[node] = Node(node.val)
            for neighbor in node.neighbors:
                mp[node].neighbors.append(dfs(neighbor))
            return mp[node]


        return dfs(node)
        