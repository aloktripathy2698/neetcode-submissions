# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        n1 = dummy
        for i in range(n + 1):
            n1 = n1.next
        
        n2 = dummy
        while n1:
            n1 = n1.next
            n2 = n2.next
        print(n2.val)
        n2.next = n2.next.next
        return dummy.next
        