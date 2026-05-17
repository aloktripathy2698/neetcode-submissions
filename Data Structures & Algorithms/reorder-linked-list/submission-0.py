
class Solution:
    def reverseList(self, l):
        prev, curr = None, l
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def mergeList(self, l1, l2):
        dummy = ListNode(-1)
        node = dummy
        flag = True
        while l1 and l2:
            if flag:
                flag = False
                node.next = l1
                l1 = l1.next
            else:
                flag = True
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        l2 = self.reverseList(l2)

        # Merge the two halves
        self.mergeList(l1, l2)
