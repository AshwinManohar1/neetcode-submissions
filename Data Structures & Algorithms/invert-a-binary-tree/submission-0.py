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

        queue = deque([root])

        while len(queue) != 0:
            e = queue.popleft()
            e.left , e.right = e.right , e.left

            if e.right is not None:
                queue.append(e.right)
            if e.left is not None:
                queue.append(e.left)

        return root

        