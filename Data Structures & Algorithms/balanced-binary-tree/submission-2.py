# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # base case
        if not root:
            return True
        
        #traverse down left and right
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)

        # math logic
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)



        # def need max height func
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
