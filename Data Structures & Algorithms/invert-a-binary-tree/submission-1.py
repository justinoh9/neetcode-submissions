# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        head = root
        
        headLeft = head.left
        headRight = head.right
        head.left = headRight
        head.right = headLeft
        # return head
        self.invertTree(head.left)
        self.invertTree(head.right)
        return head
