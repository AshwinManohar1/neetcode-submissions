# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # queue = deque([root])
        # height = 0
        # while queue:
        #     level_size= len(queue)
        #     height += 1
        #     for _ in range(level_size):
        #         e = queue.popleft()

        #         if e.left is not None:
        #             queue.append(e.left)

        #         if e.right is not None:
        #             queue.append(e.right)


        def findLength(node):

            if not node:
                return 0

            left_height = findLength(node.left)
            right_height = findLength(node.right)

            return 1 + max(left_height , right_height)


        return findLength(root)
            







        