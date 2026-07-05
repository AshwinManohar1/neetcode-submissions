# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getCommonAncestor(node):
            if not node:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left_node = getCommonAncestor(node.left)
            right_node =  getCommonAncestor(node.right)

            if left_node and right_node:
                return node

            return left_node if left_node else right_node

        return  getCommonAncestor(root)           





