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

        def dfs(u):
            if u in mp:
                return mp[u]
            nu = Node(u.val, [])
            mp[u] = nu
            for v in u.neighbors:
                nv = dfs(v)
                nu.neighbors.append(nv)
            return nu

        dfs(node)
        return mp[node]
        