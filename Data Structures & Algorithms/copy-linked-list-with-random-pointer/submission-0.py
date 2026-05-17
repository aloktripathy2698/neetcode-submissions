"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            copyNode = Node(node.val)
            temp = node.next
            node.next = copyNode
            copyNode.next = temp
            node = copyNode.next

        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        copyHead = head.next
        copyNode = copyHead
        node = head
        while node:
            node.next = copyNode.next if copyNode else None
            node = copyNode
            copyNode = copyNode.next if copyNode else None
        return copyHead

        