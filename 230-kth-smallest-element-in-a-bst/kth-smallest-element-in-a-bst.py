# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            heapq.heappush(heap,root.val)
            inorder(root.right)
        inorder(root)

        ans=0
        for i in range(k):
            ans=heapq.heappop(heap)

        return ans