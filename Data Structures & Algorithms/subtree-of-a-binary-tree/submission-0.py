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

        queue = deque([root])

        while queue:
            e= queue.popleft()
            if e.val == subRoot.val:
                if self.isSameTree(e , subRoot):
                    return True

            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)

        return False

    def isSameTree(self , p , q):

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)
        