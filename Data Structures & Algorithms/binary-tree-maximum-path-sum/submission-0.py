from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # Ignore negative paths
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update global max path sum
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # Return the max path sum going downwards
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
