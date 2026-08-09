# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def calculateDiameter(root):
            if not root:
                return 0

            left = calculateDiameter(root.left)
            right = calculateDiameter(root.right)

            calculate_diameter = left + right
            self.maxDiameter = max(self.maxDiameter,calculate_diameter)

            return 1 + max(left , right)

        calculateDiameter(root)

        return self.maxDiameter

