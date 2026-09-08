# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root , subRoot):
                return True

        search_left = self.isSubtree(root.left, subRoot)
        search_right = self.isSubtree(root.right, subRoot)

        return search_left or search_right

    def isSameTree(self, p , q):

        if not p and not q:
            return True

        if not p or not q:
            return False 

        if p.val != q.val:
            return False 

        left_match = self.isSameTree(p.left , q.left)
        right_match = self.isSameTree(p.right, q.right)

        return left_match and right_match

        

            
                
        