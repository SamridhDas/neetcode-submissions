# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            maxleft=dfs(node.left)
            maxright=dfs(node.right)
            return 1+max(maxleft,maxright)
        return dfs(root)

        