# Definition for singly-linked list.

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
           current = head
           while current:
                values.append(current.val)
                current = current.next
        values.sort()
        dummy = ListNode(0)
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next