# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # basically, check and store to compare all values of a tree

        # returning true if all values are equal

        # base case

        if not p and not q:
            return True

            
        if (p and q) and (p.val == q.val):

            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

            return left and right
        
        else:
            return False
