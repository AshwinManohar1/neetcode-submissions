class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        current_state = []

        def dfs(current_state):
            if len(current_state) == len(nums):
                res.append(current_state.copy())
                return
            
            for i in range(0 , len(nums)):

                if nums[i] in visited:
                    continue

                current_state.append(nums[i])
                visited.add(nums[i])

                dfs(current_state)


                current_state.pop()
                visited.remove(nums[i])

        dfs(current_state)

        return res
        