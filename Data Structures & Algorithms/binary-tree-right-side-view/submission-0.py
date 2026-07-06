# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        results = []
        queue = deque([root])
        level = 0
        while queue:
            level+=1
            len_size = len(queue)

            for i in range(len_size):
                e = queue.popleft()
                
                if i == len_size-1:
                    results.append(e.val)

                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)

        return results


