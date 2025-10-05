# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        mid=n//2
        new=head
        for _ in range(mid - 1):
            new = new.next
        nxt=new.next
        new.next=nxt.next
        return head