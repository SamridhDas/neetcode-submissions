# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,subroot):
            if not subroot:
                return True
            if not root:
                return False
            return same(root,subroot) or dfs(root.left,subroot) or dfs(root.right,subroot)
        def same(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val==subroot.val:
                return same(root.left,subroot.left) and same(root.right,subroot.right)
            return False
        return dfs(root,subRoot)