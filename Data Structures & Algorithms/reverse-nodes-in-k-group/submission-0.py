# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, head, groupPrev, groupNext):
        prev, curr = groupPrev, head
        while curr != groupNext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = groupNext
        groupPrev.next = prev
        groupPrev = head
        return groupPrev

    def getKthNode(self, groupPrev, k):
        node = groupPrev
        while k and node:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy
        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next
            groupPrev = self.reverseGroup(groupPrev.next, groupPrev, groupNext)
        return dummy.next



        