# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum1=0
        def dfs(node):
            nonlocal sum1
            if not node:
                return 
            dfs(node.right)
            sum1+=node.val
            node.val=sum1
            dfs(node.left)
        dfs(root)
        return root