# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow=head
        fast=head
        prev_slow=None
        while fast!=None and fast.next!=None:
            prev_slow=slow
            slow=slow.next
            fast=fast.next.next

        prev_slow.next=slow.next

        return head