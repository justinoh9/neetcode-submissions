# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # recursion

        # base case
        if not root:
            return None

        # swap

        tempLeft = root.left
        root.left = root.right
        root.right = tempLeft

        # recursive case
        # basically going down left and right nodes
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        return root