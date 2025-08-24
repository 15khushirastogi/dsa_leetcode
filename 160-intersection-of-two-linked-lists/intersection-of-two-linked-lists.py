# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        st = set()
        while head1 != None:
            st.add(head1)
            head1 = head1.next
        while head2 != None:
            if head2 in st:
                return head2
            head2 = head2.next
        return None