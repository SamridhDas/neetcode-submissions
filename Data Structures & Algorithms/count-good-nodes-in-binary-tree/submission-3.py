# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,vmax):
            if not node:
                return 0
            if node.val>=vmax:
                res=1
            else:
                res=0
            vmax=max(vmax,node.val)
            res+=dfs(node.left,vmax)
            res+=dfs(node.right,vmax)
            return res
        return dfs(root,float('-inf'))