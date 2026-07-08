# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder and not inorder:
            return None

        root_ele = preorder[0]
        root = TreeNode(root_ele)
        # find root_ele in inorder
        inorder_ele_index = inorder.index(root_ele)

        left_inorder = inorder[:inorder_ele_index]
        right_inorder = inorder[inorder_ele_index+1:]

        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder )

        return root
        