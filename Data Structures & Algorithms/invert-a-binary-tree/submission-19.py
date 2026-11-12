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
        # create queue for bfs
        queue = deque([root])

        while queue:
            # analyze curr node
            node = queue.popleft()
            # perform swap on curr
            node.left, node.right = node.right, node.left
            # add children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
            