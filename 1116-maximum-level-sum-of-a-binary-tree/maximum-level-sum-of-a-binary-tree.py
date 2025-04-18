# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        smallest_level=float('inf')
        maximalSum=float('-inf')
        q=deque()
        q.append([root,1]) #[node,level]
        while q:
            size=len(q)
            levelsum=0
            for i in range(size):
                node,level=q.popleft()
                levelsum+=node.val
                if node.left:
                    q.append([node.left,level+1])
                if node.right:
                    q.append([node.right,level+1])

            if levelsum>maximalSum:
                maximalSum=levelsum
                smallest_level=level

        return smallest_level