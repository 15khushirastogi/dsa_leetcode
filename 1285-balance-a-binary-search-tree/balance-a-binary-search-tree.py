# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            newnode = TreeNode(inorder[mid])
            newnode.left = build(start, mid - 1)
            newnode.right = build(mid + 1, end)
            return newnode

        return build(0, len(inorder) - 1)
