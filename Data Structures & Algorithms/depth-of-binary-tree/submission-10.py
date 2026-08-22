# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        # recursive again

        # base case
        if not root:
            return 0
        
        # rec case
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        res = max(res, left, right)

        return 1+res