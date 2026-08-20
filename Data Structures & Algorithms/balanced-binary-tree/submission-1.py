# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # now use height function 
        left = self.height(root.left)
        right = self.height(root.right)
        # then, we have the height of both the current left and current right nodes
        if abs(left - right) > 1: # if the difference in height between those nodes are greater than one, 
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    # first, implmenet height function
    def height(self, root: optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
