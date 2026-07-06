# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        queue = deque([(root, root.val)])

        while queue:
            e , max_so_far = queue.popleft()

            if e.val >= max_so_far:
                count+=1

            new_max = max(max_so_far ,e.val)

            if e.left is not None:
                queue.append((e.left, new_max))
            if e.right is not None:
                queue.append((e.right, new_max))

        return count

        