# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_path_value = float('-inf') 

        def getPathValue(node):

            if not node:
                return 0

            left_sum = max(getPathValue(node.left), 0)
            right_sum =max(getPathValue(node.right), 0)

            return node.val + max(left_sum , right_sum)


        def traverseAllNodes(node):
            if not node:
                return

            left_branch = max(getPathValue(node.left),0)
            right_branch = max(getPathValue(node.right), 0)

            current_path_sum = node.val + left_branch + right_branch

            self.max_path_value = max(self.max_path_value , current_path_sum)


            traverseAllNodes(node.left)
            traverseAllNodes(node.right)
        
        traverseAllNodes(root)

        return self.max_path_value


        
        

            

        