# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        # kind of implement dfs, but this time i need to use res = 0 and nonlocal

        res = 0

        def dfs(root):
            nonlocal res
            # base case
            if not root:
                return 0
            
            # do da dfs thing
            #left
            left = dfs(root.left)
            #right
            right = dfs(root.right)
            #res
            res = max(res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return res 