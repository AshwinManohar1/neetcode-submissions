class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        subset = []

        def dfs(current_index):

            if current_index >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[current_index])
            dfs(current_index+1)

            subset.pop()
            dfs(current_index+1)

        dfs(0)
        return res