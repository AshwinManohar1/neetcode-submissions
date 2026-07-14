class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current_combination = []
        def dfs(i , current_sum):
            # base
            if current_sum == target:
                res.append(current_combination.copy())
                return

            if i>= len(nums) or current_sum > target:
                return

            # append
            current_combination.append(nums[i])

            dfs(i ,current_sum+nums[i])

            #dele

            current_combination.pop()
            dfs(i+1, current_sum)

        dfs(0 , 0)
        return res

            

