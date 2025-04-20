# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        q.append([root,1])
        height=1
        while q:
            node,curheight=q.popleft()
            height = max(height, curheight)
            if node.left:
                q.append([node.left,curheight+1])
            if node.right:
                q.append([node.right,curheight+1])

        return height

