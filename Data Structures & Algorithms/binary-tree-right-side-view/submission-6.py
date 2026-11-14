# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # basically go level by level
        # keep track of the right most node of each level
        # create a list of those node's values from top to bottom

        if not root:
            return []
        res = []
        
        q = deque([root])
        while q:
            # iterate each level completely
            levelMax = -100
            for _ in range(len(q)):

                node = q.popleft()
                if node:
                    levelMax = max(levelMax, node.val)
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)

            res.append(levelMax)
        
        return res
