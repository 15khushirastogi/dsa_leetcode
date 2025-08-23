# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalNodes=0
        cur=head
        while cur:
            totalNodes+=1
            cur=cur.next
        pos=totalNodes-n
        if pos == 0:
            nodeToDelete = head
            head = head.next
            del nodeToDelete
            return head
        i=1
        newcur=head
        while newcur:
            if i==pos:
                break
            newcur=newcur.next
            i+=1
        nodeToDelete=newcur.next
        newcur.next=nodeToDelete.next

        del nodeToDelete

        return head