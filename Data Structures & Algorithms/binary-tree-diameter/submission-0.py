# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def findLength(root):
            nonlocal max_diameter
            if not root:
                return 0

            left_max = findLength(root.left)
            right_max = findLength(root.right)

            current_diameter = left_max + right_max

            max_diameter = max(current_diameter , max_diameter)

            return 1 + max(left_max , right_max)
        findLength(root)
        return max_diameter
