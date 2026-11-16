
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the Nth node from the end
        slow.next = slow.next.next

        return dummy.next
