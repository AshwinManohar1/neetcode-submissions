# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # queue = deque([root])
        # result = []
        # while queue:
        #     level = []
        #     len_size = len(queue)

        #     for _ in range(len_size):
        #         e = queue.popleft()
        #         level.append(e.val)

        #         if e.left is not None:
        #             queue.append(e.left)
        #         if e.right is not None:
        #             queue.append(e.right)
        #     result.append(level)
        # return result

        # if not root:
        #     return []

        # queue = deque([root])
        # result = []

        # while queue:
        #     level = []
        #     len_size = len(queue)

        #     for _ in range(len_size):
        #         e = queue.popleft()
        #         level.append(e.val)
        #         if e.left is not None:
        #             queue.append(e.left)
        #         if e.right is not None:
        #             queue.append(e.right)
        #     result.append(level)
        # return result
        res = []

        def dfs(node , depth):

            if not node:
                return None

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left , depth+1)
            dfs(node.right, depth+1)

        result = dfs(root , 0)

        return res

